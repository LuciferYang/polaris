/*
 * Copyright (c) 2024 Snowflake Computing Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.polaris.core.persistence.cache;

import org.jetbrains.annotations.Nullable;

/** Result of a lookup operation */
public class EntityCacheLookupResult {

  // if not null, we found the entity and this is the entry. If not found, the entity was dropped or
  // does not exist
  private final @Nullable EntityCacheEntry cacheEntry;

  // true if the entity was found in the cache
  private final boolean cacheHit;

  public EntityCacheLookupResult(@Nullable EntityCacheEntry cacheEntry, boolean cacheHit) {
    this.cacheEntry = cacheEntry;
    this.cacheHit = cacheHit;
  }

  public @Nullable EntityCacheEntry getCacheEntry() {
    return cacheEntry;
  }

  public boolean isCacheHit() {
    return cacheHit;
  }
}
