<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0825.txt",
      "sha256": "4f60672bdedacedb21fc3df524f67c15dfb5b790028c9761d759e8c259f55c5a",
      "bytes": 13543
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ec0f66324d42f268dd4b029c8a28738515a6081d4c053bb5356bf9809afd5e35",
      "bytes": 1942
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3aa845c898a4d7baa3b82163a8c21152b9cc8866113c3b3793c09c7a03e2878f",
      "bytes": 226544
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "10b8f782a7c21c620a774a51b4a25c867d5ead81e8afd13921395bfd3d783b8d",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "2a656cd82aee6e9210fcf904fcf772a057dd588adbdba20f9466e1359656e44a",
      "bytes": 831
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "e0211136baa64ea126e86410801bc744236294d98fd393e4f94b9134e1e6b48b",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "30847da0b121aba94cdc65bbbf367fc0c6ad6e7d5a977cb0b1639055ed469e50",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a2a29edb7ced36097f766776b4b7adc6a664966c328a437b661bcc87ca9df67c",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "add263ff47c3c08c02ffe20daba85c1a21e9f7476eaa2572157d9cc8940fac59",
      "bytes": 820
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d6eb10505e3ae21e2634e74e87280a075a9e5c9524aeeb977b2ad32b3670e66a",
      "bytes": 250419
    }
  ],
  "estimated_tokens": 10341
}
-->

# Durable State Update — Chapter 825

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 825. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 825. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 825,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 825,
    "continuity_sources": [825],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades, including under the name Muninn.",
    "The Doppelganger can resurrect by consuming absorbed lives and reproduce absorbed people’s appearances, abilities, and memories; it has taken Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger’s absorbed lives were dwindling after it forced Blink beyond its normal range; it has now killed twenty of its followers and absorbed their vitality and souls.",
    "The Doppelganger confirmed Jin is the Chosen One and believes its master will be pleased.",
    "Blue-white flames erupted above the ruined oil field where the Doppelganger arrived; their source and effect are unknown.",
    "Jin defeated Hamid Shah Masoud and ended the battle against the fanatics, but his Middle Dantian is at its limit and his mental strength is depleted.",
    "Jin and the Skeleton King pursued the Doppelganger by Teleport; Magic Johnson stayed behind to guard the battlefield."
  ],
  "continuity_sources": [
    823,
    824
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "What caused the blue-white flames, and what happened to the Doppelganger?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 824,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 몬스터     | **monster**           |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 824
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 824
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** Not established
- **Relationships:** It served an unnamed master who sent it to this world and ordered it to avoid the target until the master’s plan was complete; it regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 824
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 824
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 824
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 820
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃825화



텔레포트 마법과 함께 터져 나온 아득한 섬광.

그것이 시작이었다.

주위의 공간이 일그러진다. 지금껏 느껴본 적 없는 끔찍한 압박감이 심장을 움켜쥐고, 제3의 허공으로 빨려 들어간 관절과 근육이 비명을 내지른다.

‘흡.’

숨이 막혔다. 고통스러웠다.

불과 몇 초도 되지 않는 짧은 시간이 마치 며칠이라도 된 것처럼 길게 느껴졌다.

하지만 나는 끊어지려는 의식의 끈을 붙잡고 매달렸다.

까득.

견뎌야 한다. 반드시 버텨야 한다.

오직 그 일념(一念)으로 이를 악물었다. 시야를 물들인 휘황한 빛줄기 사이로, 쉴 새 없이 뒤집히는 땅과 하늘이 스쳐 지나갔다.

드넓은 황야. 초승달처럼 굽이진 언덕으로 이어진 사막.

수백 킬로미터가 넘는 거리가 순식간에 지워지고, 거칠게 요동치던 섬광이 빠르게 사그라졌다.

그리고 마침내 짙은 어둠이 내려앉았을 때.

화아악.

공간이 갈라졌다. 그 틈새 너머로 조금 전의 섬광과는 다른 새로운 빛이 스며들었다.

아니, 새로운 것은 비단 그뿐만이 아니다.

‘이건…….’

보인다. 느껴진다.

어둡지도, 밝지도 않은 어스름한 빛과 축축한 새벽 공기.

바람에 섞인 모래알, 거기에 더해 마력(魔力)만이 지닌 특유의 끈적하고 불쾌한 감각까지.

‘됐다.’

나는 직감했다.

이 위험천만한 시도가 성공했다는 것을.

대마도사가 발휘한 텔레포트 마법이 마력의 방해를 뚫고 정해진 좌표로 우리를 인도했다는 것을.

그리고 마침내 도달한 그 낯선 공간 너머에, 그토록 찾아 헤매던 한 존재가 있었다.

도플갱어(Doppelganger).

“……!”

허공에서 맞닥트린 시선. 동시에 커지는 눈동자.

나는 도플갱어를, 도플갱어는 나를 바라보았다.

마치 세상이 멈춘 것처럼 시간이 느릿하게 흘렀다.

그러나 이미 해야 할 일을 알고 있는 몸은 시간과 공간을 거스르며 나아갔다.

슈확.

창날을 타고 좌우로 갈라진 바람이 귓가를 스친다.

손아귀에 틀어쥔 백염(白炎)의 창대를 뒤로 젖히자, 뼈가 어긋나는 소리와 함께 예상치 못했던 통증이 밀려들었다.

우두둑.

불안정했던 텔레포트 마법의 후유증이다.

고작 수백 미터를 이동했던 도플갱어의 블링크 마법과는 달리, 수백 킬로미터를 뛰어넘은 위험한 시도의 대가는 고스란히 몸뚱어리가 치러야 했다.

‘빌어먹을.’

호흡이 끊기고 손끝이 흔들린다. 창날 위로 내달리던 열양지기가 몸의 이상을 눈치채고 주춤거리는 것이 느껴졌다.

하지만 그 모든 것은 기우(杞憂)에 불과했다.

지금의 나는 혼자가 아니었으니까.

툭.

강한 힘이 실린 단단한 손이 등을 짚었다. 스켈레톤 킹의 또렷한 음성이 귓가를 파고들었다.

- 가라.

그 순간.

후웅!

나는 쏘아졌다.

텔레포트 마법이 벌린 공간의 틈새를 찢고, 벼락처럼 내리꽂혔다. 잠시 주춤하던 열양지기가 들불처럼 일어나 창날을 휘감았다.

화륵.

뜨거운 열기가 퍼져 나간다. 십여 미터의 공간이 단숨에 지워진다.

그리고 그 끝에, 이 예상치 못한 상황 앞에서 눈을 부릅뜬 채 선 도플갱어가 있었다.

“이……!”

무슨 말을 하려 했을까. 무슨 말이 그토록 하고 싶었을까.

하지만 그 누구도, 심지어 놈조차도 그 뒷말을 들을 수 없었다.

아니, 이을 수 없었다.

콰아아아!

파도처럼 터져 나온 청백색의 화염이, 채 끝맺지 못한 외침과 함께 도플갱어의 몸뚱어리를 집어삼켰다.



* * *



도플갱어는 몸부림쳤다.

그것은 지금껏 겪었던 무수한 죽음 중에서도 손꼽힐 만큼 끔찍한 고통이었고, 진정한 의미의 화마(火魔)였다.

서걱. 화아악.

상반신을 비스듬히 가르고 지나간 창날과 함께, 용암 같은 기운이 도플갱어의 전신 곳곳으로 스며들어 몸부림쳤다.

죽음과 동시에 빈 자리를 차지한 생명력을 계속해서 갉아먹으며.

피를 증발시키고, 살과 뼈를 녹이며.

“크아아아악!”

도플갱어는 고통에 찬 비명을 토해 냈다.

몸 안으로 침투한 화염은 이미 십여 개의 목숨을 잿더미로 만들었다. 끊임없이 회복되는 살과 뼈가 소방관 역할을 해 주지 않았다면, 지금 이 순간조차도 죽어 가고 있었을 것이다.

“끄으으.”

실핏줄이 터져 나가 붉게 물든 눈동자.

도플갱어가 고통 어린 신음과 함께 허리를 편 그 순간.

쐐액, 푹!

비틀거리던 몸을 가누기도 전에 날아든 무언가가 미간을 관통한다.

뒤로 기울어지던 신형이 지면에 닿기도 전에 부활한 도플갱어가 황급히 옆으로 몸을 날렸다.

푸푸푸푹!

아슬아슬하게 몸뚱어리를 스치며 지면에 틀어박히는 새하얀 무언가.

그것들의 정체가 뼛조각이라는 것을 파악한 도플갱어가 고개를 들었다.

더없이 익숙하면서도, 한편으로는 이질적인 기운을 지닌 존재가 그를 향해 쇄도하고 있었다.

‘저놈은……!’

스켈레톤 킹.

한낱 언데드 몬스터에게는 과분한, 그러나 결코 무시할 수 없는 기운이 실린 검신이 번뜩였다.

서걱!

예리한 절삭음.

[영웅의 검]이라는 이름과는 전혀 어울리지 않는, 휘황한 빛을 흩뿌리는 마력이 손목을 가른다.

격통과 함께 물러난 도플갱어가 사나운 목소리로 부르짖었다.

“감히 언데드 따위가……!”

무수한 몬스터가 존재하는 마계(魔界)에서도 언데드의 위치는 맨 밑바닥.

이미 지고한 영역에 오른 뒤에야 스스로 언데드가 되기를 선택한 리치(Lich) 같은 존재가 아니라면, 언데드는 한낱 병졸에 불과했다.

아니, 분명 그럴 터였다.

퍼걱, 촤아아악!

눈부신 검광과 함께 터져 나오는 핏물.

순식간에 또 한 번의 죽음을 맞이한 도플갱어가 이를 악물었다.

‘빌어먹을.’

짧은 공방이었지만 내심 인정할 수밖에 없었다. 스켈레톤 킹은 결코 쉬운 상대가 아니라는 것을.

눈앞의 저 변종이, 평범한 언데드의 한계를 깨트리고 높은 격에 다다른 존재라는 것을.

하지만…….

‘저 괴물만큼은 아니지.’

스켈레톤 킹을 피해 훌쩍 물러난 도플갱어의 시선이 빠르게 움직였다.

깊숙이 가라앉은 그의 눈동자에, 한 자루의 창을 지팡이 삼아 거칠게 호흡을 몰아쉬는 진태경의 모습이 비쳤다.

‘마지막으로 봤던 것과는 다르다. 놈도 한계 이상의 힘을 사용한 것이 분명해.’

도플갱어는 우둔하지 않다.

아니, 여느 인간이나 몬스터와 비교해도 월등하게 교활했다.

지난 수십여 년간 미카엘 실베르트라는 허수아비의 뒤에 숨어 세상을 주무를 만큼.

그리고 조금 전 갑작스럽게 나타난 진태경의 일격 앞에서도, 지크프리트 바스만의 영혼을 다른 것으로 바꿔치기할 만큼.

‘깃들어라.’

콰아아.

도플갱어를 중심으로 휘몰아치는 강렬한 바람. 심상치 않은 기세를 느낀 스켈레톤 킹이 지면을 박차며 손을 뻗었다.

슈확!

팔의 뼈 일부가 날카로운 파공성과 함께 공간을 갈랐다. 마치 암기처럼 날아든 새하얀 뼛조각들이 도플갱어의 전신에 틀어박혔다.

아니, 스켈레톤 킹의 눈에는 그렇게 보였다.

피를 흩뿌리며 쓰러져야 했을 도플갱어의 신형이, 마치 처음부터 그 자리에 없었던 것처럼 지워지기 전까지는.

팟.

사라졌다. 말 그대로 눈 깜빡할 사이에.

그리고 그것은 한 가지 사실을 의미했다.

마법.

‘블링크(Blink)?’

스켈레톤 킹은 불현듯 찾아온 깨달음과 동시에 본능적으로 몸을 비틀었다.

그러나 찰나의 순간 허를 찔러 시야를 벗어난 도플갱어는, 이미 그다음을 준비하고 있었다.

그그그극.

느려진 세상 속에서 마나가 격동한다.

그 중심에는 생전 위대했던 대마도사의 모든 것을 탐욕스럽게 집어삼키고, 흡수하여 자신의 배를 불린 몬스터가 있었다.

‘에어 슬래시(Air Slash).’

그 순간.

슈화아아악!

스켈레톤 킹을 향해 빗발치는 바람의 칼날을 바라보며, 도플갱어는 확신했다.

저것이 당장 저 변종을 소멸시키지는 못하더라도, 잠시나마 전투 불능 상태로 빠트릴 수 있을 만큼 위력적인 마법이라고.

이 지긋지긋한 싸움을 끝낼 수 있으리라고.

하지만 착각이었다.

스켈레톤 킹이 순간적으로 도플갱어를 시야에서 놓쳤듯이, 도플갱어 역시 한 사람의 존재를 망각하고 있었으니.

화륵.

십여 미터 위 허공에 떠올라 있던 도플갱어는, 문득 자신을 향해 솟구치는 열기를 느꼈다.

그제야 조금 전까지만 하더라도 제 몸조차 제대로 가누지 못하고 있던 누군가가 떠올랐다.

‘이런 미친……!’

헛숨을 삼킨 도플갱어가 황급히 마나를 되돌린 순간.

후욱.

스켈레톤 킹을 집어삼킬 듯이 떨어져 내리던 광풍(狂風)이 산들바람이 되어 흩어졌다. 동시에 반투명한 방어막이 도플갱어의 전신을 겹겹이 뒤덮었다.

그리고 공간을 가로질러 날아든 눈부신 섬광이, 마침내 방어막의 표면과 맞닿은 그때.

콰직!

도플갱어는 똑똑히 들을 수 있었다. 볼 수 있었다.

수십 겹의 실드 마법을 파고드는 한 줄기의 불꽃과, 산산이 부서지는 마나의 방패를.

꽈아아앙!

발화. 분쇄. 폭발.

세 가지 일이 동시에 일어났고, 허공을 물들인 청백색의 화염과 함께 거대한 충격파가 사방을 후려쳤다.

구구구구궁!

지면까지 고스란히 전해지는 충격을 느낀 스켈레톤 킹은 찰나의 순간 생각했다.

어쩌면 지금의 일격으로, 도플갱어는 가장 귀중한 영혼 중 하나를 잃었을지도 모르겠다고.

그러나 진태경은 아니었다.

힘든 와중에도 젖 먹던 힘까지 끌어 올려 일격을 날린 그는 누구보다 정확하게 알고 있었다.

이제는 익숙해져 버린 맑은 종소리가, 왜 지금만큼은 들리지 않는지.

‘아직, 아직이다.’

놈은, 도플갱어는 아직 대마도사의 힘과 영혼을 지니고 있다.

하지만 진작 힘차게 지면을 박찼어야 할 두 다리가 움직이지 않았다.

바닥난 심력(心力)은 그의 의식을 자꾸만 무저갱으로 끌어당겼고, 지금 이 순간 머릿속에 떠오르는 수십여 개의 움직임과 공격 루트는 실현할 수 없는 상상에 불과했다.

다만, 눈빛을 마주한 것만으로도 서로의 마음을 읽을 수 있는 친구가 있을 뿐.

쾅!

찰나의 순간 허공에서 교차된 시선.

그러나 그것만으로 충분했다. 진태경의 눈동자에 담긴 뜻을 읽어 낸 스켈레톤 킹은 한 치의 망설임도 없이 지면을 박차고 솟구쳤다.

허공을 가득 메운 매캐한 연기 사이로.

폭발의 중심에 있을 도플갱어를 향해.

츠츠츠츠!

황금빛 마력이 검신을 타고 흘러넘친다.

무리한 텔레포트 마법의 여파로 인해 평소의 절반도 되지 않는 위력이었지만, 눈부신 검광(劍光)은 거침없이 하늘을 갈랐다.

짙은 연기를 베어 내고 그 너머에 있을 적을 향해 쏘아졌다.

쉭!

한 줄기의 섬광.

그 첨예한 일격의 끝에.

서걱!

분수처럼 터져 나오는 선홍빛 핏물이 있었다.



* * *



비록 서서히 흐릿해져 가는 시야였지만, 똑똑히 보았다.

허공을 가로지르는 스켈레톤 킹의 일격을. 그리고 핏물과 함께 솟구친 누군가의 팔을.

‘베었다.’

틀림없다. 새하얗고 가느다란 저 팔은 도플갱어의, 정확히 말하자면 이미 삼 년 전 놈에게 흡수당한 대마도사의 것이 분명하다.

하지만 응당 떨어져야 했을 목도, 터져 나와야 했을 비명도 어디에도 없었다.

만약 또 다시 시야에서 사라진 도플갱어의 위치를 파악하지 못했다면, 한바탕 고함을 내질렀을지도 모른다.

그러나 나는 분노를 표출하는 대신 억눌렀다.

남의 것처럼 낯선, 피로에 지친 목소리가 입술 사이로 흘러나왔다.

“네가 무슨 도마뱀이냐, 이 씨벌놈아?”

천천히 몸을 돌리자, 폐허 한가운데에 서 있는 도플갱어의 모습이 보였다. 깔끔하게 절단된 한쪽 어깻죽지에서는 피가 펑펑 쏟아지고 있었다.

“이번에는 머리로 하자. 팔이나 다리 말고, 네 머리통. 어때?”

“그건 곤란할 것 같군.”

악귀처럼 일그러진 얼굴로 대답한 도플갱어가 말을 이었다.

“앞으로의 일을 위해서는, 대마도사의 영혼이 반드시 필요하거든.”

뭐?

나도 모르게 반문하려던 그 순간.

우우웅.

놈을 중심으로 거대한 기운이 맥동했다.

아니, 폐허 전체가 살아 있는 생물처럼 몸을 떨었다.
```

## Final English reading copy

```markdown
# Chapter 825

A distant flash burst forth with the Teleport spell.

That was how it began.

The space around me warped. A horrifying pressure unlike anything I’d ever felt seized my heart, and my joints and muscles, sucked into a third void, screamed.

*Hngh.*

I couldn’t breathe. It hurt.

A brief span of less than a few seconds felt as long as days.

But I clung to the thread of my consciousness, just as it was about to snap.

*Crack.*

I had to endure. I had to hold on, no matter what.

Clenching my teeth with that single thought, I watched the ground and sky flip endlessly past through the dazzling beams of light that flooded my vision.

A vast wilderness. A desert stretching toward hills curved like a crescent moon.

A distance of hundreds of kilometers vanished in an instant, and the violently churning flash quickly faded.

And at last, when deep darkness settled over us—

*Fwoosh.*

Space split open. Beyond the gap, a new light—different from the flash moments ago—began to seep in.

No, it wasn’t the only thing that was new.

*This is…*

I could see it. I could feel it.

The dim light, neither dark nor bright, and the damp air of early morning.

Sand grains mingled with the wind—and, on top of that, the uniquely sticky, unpleasant sensation that belonged only to magical power.

*We did it.*

I knew it instinctively.

This perilous attempt had succeeded.

The Grand Mage’s Teleport spell had overcome the magical power interfering with it and brought us to the designated coordinates.

And beyond that unfamiliar space we’d finally reached was the being we’d searched for so desperately.

The Doppelganger.

“……!”

Our eyes met in midair. At the same moment, our pupils widened.

I looked at the Doppelganger, and the Doppelganger looked at me.

Time crawled by, as if the world had come to a stop.

But my body already knew what it had to do. It pushed forward, defying time and space.

*Whoosh.*

Wind split to either side along the spearhead, brushing past my ears.

As I pulled back the shaft of White Flame, gripped tightly in my hand, an unexpected pain surged through me with the sound of bones shifting out of place.

*Crack.*

It was an aftereffect of the unstable Teleport spell.

Unlike the Doppelganger’s Blink spell, which had moved it only a few hundred meters, this dangerous attempt had hurled us hundreds of kilometers. My body had to bear the full cost.

*Fuck.*

My breath hitched, and my fingertips trembled. I could feel the Scorching Yang Qi racing along the spearhead falter as it sensed something was wrong with my body.

But all of that was needless worry.

Because I wasn’t alone.

*Thump.*

A firm hand, backed by tremendous strength, pressed against my back. The Skeleton King’s clear voice pierced my ears.

“Go.”

In that instant—

*Whoom!*

I shot forward.

Tearing through the gap in space opened by the Teleport spell, I plunged down like a bolt of lightning. The Scorching Yang Qi, which had faltered for a moment, rose like a wildfire and coiled around the spearhead.

*Fwoosh.*

Seething heat spread out. Ten-odd meters of space vanished in an instant.

And at the end of it stood the Doppelganger, eyes wide at this unexpected turn of events.

“Y—!”

What had it been trying to say? What had it wanted so badly to say?

But no one—not even the bastard itself—could hear the rest of it.

No. It couldn’t finish.

*KWA-BOOM!*

Blue-white flames erupted like a wave and swallowed the Doppelganger’s body along with its unfinished cry.

* * *

The Doppelganger writhed.

Among the countless deaths it had experienced, this was one of the most terrible pains it had ever endured. It was fire in the truest sense.

*Shhk. Fwoosh.*

Along with the spearhead that had slashed diagonally across its upper body, a lava-like force seeped into every part of the Doppelganger’s body and rampaged through it.

Even as it died, that force continued gnawing away at the life force that took the place of each life it lost.

It vaporized its blood and melted its flesh and bones.

“GRAAAAH!”

The Doppelganger let out a scream of agony.

The flames that had penetrated its body had already reduced more than ten lives to ash. If its endlessly regenerating flesh and bones hadn’t acted as firefighters, it would still be dying at that very moment.

“Grrr…”

Its bloodshot eyes were red with burst blood vessels.

The moment the Doppelganger groaned in pain and straightened up—

*Whizz—thunk!*

Before it could steady its unbalanced body, something came flying and pierced its forehead.

The Doppelganger revived before its body, falling backward, could touch the ground, then hurriedly threw itself to the side.

*Thud-thud-thud!*

Something pure white grazed its body and embedded itself in the ground.

Realizing the objects were pieces of bone, the Doppelganger lifted its head.

A being with a power both utterly familiar and strangely alien was rushing toward it.

*That thing…!*

The Skeleton King.

A sword imbued with power far too great for a mere undead monster—but impossible to dismiss—flashed.

*Shhk!*

A sharp slicing sound.

Magical power scattered dazzling light, utterly at odds with the name **Hero’s Sword**, as it cut through the Doppelganger’s wrist.

The Doppelganger recoiled in pain and roared in a savage voice.

“How dare an undead like you…!”

Even in the Demon Realm, where countless monsters existed, undead were at the very bottom.

Unless they were beings like Liches, who chose to become undead only after reaching the highest realm, they were mere foot soldiers.

No, that was how it was supposed to be.

*Crack—splash!*

Blood erupted with a blinding flash of the sword.

The Doppelganger met death once more in an instant and clenched its teeth.

*Damn it.*

The exchange had been brief, but it had no choice but to admit it.

The Skeleton King was no easy opponent.

That aberration before it had broken through the limits of an ordinary undead and reached a higher level of existence.

But…

*It’s still no match for that monster.*

The Doppelganger leapt far back to get away from the Skeleton King and quickly shifted its gaze.

In its sunken eyes, it saw Jin Taekyung breathing hard, using a spear as a cane.

*He’s different from the last time I saw him. He definitely used more power than his limits should allow.*

The Doppelganger wasn’t foolish.

In fact, it was far more cunning than any human or monster.

It had spent decades manipulating the world from behind Michael Silbert, a mere puppet.

And even when Jin Taekyung had appeared out of nowhere and struck, it had managed to swap Siegfried Bassman’s soul for another.

*Take hold.*

*KWA-AAH.*

A fierce wind whipped around the Doppelganger. Sensing the ominous aura, the Skeleton King kicked off the ground and reached out.

*Whoosh!*

Part of his arm bone cut through space with a sharp whistle. The pure white pieces of bone, flying like hidden weapons, embedded themselves throughout the Doppelganger’s body.

Or so it seemed to the Skeleton King.

The Doppelganger’s body, which should have fallen in a spray of blood, vanished as if it had never been there in the first place.

*Pop.*

It was gone. Literally in the blink of an eye.

And that meant one thing.

Magic.

*Blink?*

As realization struck, the Skeleton King instinctively twisted his body.

But the Doppelganger, which had caught him off guard for an instant and slipped out of his sight, was already preparing its next move.

*Grrrrk.*

Mana surged in a world that had slowed down.

At its center was the monster that had greedily swallowed up everything belonging to the Grand Mage, once a great man in life, and grown fat by absorbing it all.

*Air Slash.*

At that moment—

*Whoooosh!*

Watching blades of wind rain down on the Skeleton King, the Doppelganger was certain.

Even if they couldn’t erase that aberration outright, the spell was powerful enough to leave it unable to fight for a while.

It could end this wretched battle.

But it was mistaken.

Just as the Skeleton King had briefly lost sight of the Doppelganger, the Doppelganger had also forgotten the presence of one person.

*Fwoosh.*

Floating more than ten meters in the air, the Doppelganger suddenly felt heat surging toward it.

Only then did it remember someone who, just moments ago, hadn’t even been able to control his own body properly.

*You’ve got to be fucking kidding me…!*

The Doppelganger sucked in a startled breath and hurriedly drew back its mana.

*Whoosh.*

The gale that had been descending as if to swallow the Skeleton King scattered into a gentle breeze. At the same time, translucent shields layered over the Doppelganger’s entire body.

Then, just as a dazzling flash shot across the space and finally struck the surface of the shields—

*Crack!*

The Doppelganger heard it clearly. It saw it.

A single flame piercing through dozens of layers of Shield magic, and the mana barriers shattering into pieces.

*KWA-BOOM!*

Ignition. Shattering. Explosion.

All three happened at once, and a massive shock wave lashed out in every direction alongside blue-white flames that filled the air.

*Rumble-rumble-rumble!*

Feeling the impact travel all the way through the ground, the Skeleton King thought for the briefest instant:

Perhaps that strike had cost the Doppelganger one of its most precious souls.

But Jin Taekyung knew better.

Even in his exhaustion, he’d summoned every last bit of strength and struck. He knew better than anyone why the familiar, clear chime wasn’t ringing now.

*Not yet. Not yet.*

The bastard—the Doppelganger—still had the Grand Mage’s power and soul.

But his legs, which should already have kicked off the ground with all their might, wouldn’t move.

His depleted mental strength kept dragging his consciousness toward the abyss, and the dozens of movements and attack routes that flashed through his mind at that moment were nothing but impossible imaginings.

There was only one friend who could understand what he meant just by meeting his eyes.

*Bang!*

Their gazes crossed in midair for the briefest instant.

But that was enough. Reading the intent in Jin Taekyung’s eyes, the Skeleton King launched himself off the ground without a moment’s hesitation.

Through the acrid smoke that filled the air.

Toward the Doppelganger, at the center of the explosion.

*Tssssss!*

Golden magical power surged along the blade.

The force was less than half of what it would normally have been, thanks to the aftermath of the reckless Teleport spell. But the dazzling sword light cut through the sky without hesitation.

It sliced through the thick smoke and shot toward the enemy beyond.

*Shing!*

A single streak of light.

At the end of that keen strike—

*Shhk!*

A fountain of crimson blood burst forth.

* * *

Though my vision was slowly blurring, I saw it clearly.

The Skeleton King’s strike cutting through the air. And someone’s arm shooting up through the blood.

*He cut it off.*

No doubt about it. That slender white arm belonged to the Doppelganger—or, more precisely, to the Grand Mage the bastard had absorbed three years ago.

But there was no head that should have fallen, no scream that should have torn through the air.

If I hadn’t figured out where the Doppelganger had gone after vanishing from sight again, I might have let out a full-throated yell.

But instead of venting my anger, I held it in.

A voice, exhausted and unfamiliar, as if it belonged to someone else, slipped between my lips.

“Are you a fucking lizard or something? You son of a bitch.”

I slowly turned around. The Doppelganger stood in the middle of the ruins. Blood poured from its cleanly severed shoulder.

“Let’s try your head this time. Not your arm or leg—your whole damn head. How’s that?”

“I’m afraid that won’t be possible.”

The Doppelganger replied, its face twisted like a Fiend, then continued:

“I need the Grand Mage’s soul for what comes next.”

What?

Just as I was about to blurt out a question—

*Vwoom.*

A tremendous force pulsed around the bastard.

No—the entire ruin shuddered like a living creature.
```
