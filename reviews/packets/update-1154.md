<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1154.txt",
      "sha256": "bdec3dd5d2c8cc52b941e7a94fdec99548e3c7ec859ae8f8438929ecd64838f8",
      "bytes": 11490
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9104c159f65296afbbf8a99bee2c225af3954c15585b0eeea5c1f712e1125b85",
      "bytes": 974
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c31e0f17240cb9e8f9287b2ca17d81955d3b321295f92723889933610e52c078",
      "bytes": 246811
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "dd64595859f490ee2dec4eb6900605beacdadcbb776cb10aef9c8b8d25ccdf05",
      "bytes": 777
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0140785acc9d8913cc3cc3df1f0392706a27329390bdf024e1ee79cf74a23c84",
      "bytes": 760
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "20070e3148065860b7a98e93542d7ffb0a4e543f46596167c833e931babdf1df",
      "bytes": 668
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fef1c7d51da5fa01f4a98b1ed3c3aa73797e63a944b0c8b7455118858c740ef2",
      "bytes": 1717
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "72af007de4fb8bd0bf391e113a942db4d62407747d3216a06619b11c99cdc22a",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "4cd61566c2f8c79284fd103ca1005aa400cc31fe3ac15d2f13033495acf904bf",
      "bytes": 700
    },
    {
      "path": "characters/Michael.md",
      "sha256": "4266acf02b6aaab6e84fc2f452313ccc2ac445a18753f6136fe19f4ab717d320",
      "bytes": 821
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "52d277957d0f8dcf634e6a194d82e99e1425b11336d44df255be2ba473fafc80",
      "bytes": 293106
    }
  ],
  "estimated_tokens": 9439
}
-->

# Durable State Update — Chapter 1154

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
1 and safe_through 1154. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1154. Profile updates may replace only one
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
  "chapter": 1154,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1154,
    "continuity_sources": [1154],
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
    "Morgoth destroyed Moscow and created a Dragon Lair over its ruins; his attack caused catastrophic casualties and displacement worldwide.",
    "Morgoth offers survival to those who surrender and destruction to those who resist; twenty-three countries have surrendered.",
    "Cheon Taemin remains comatose, and the United States’ preparations against monsters depended on him.",
    "Jin Taekyung has returned, and his return was announced internationally."
  ],
  "continuity_sources": [
    1152,
    1153
  ],
  "open_questions": [
    "How will humanity respond to Morgoth’s offers of surrender?",
    "Can Jin Taekyung stop Morgoth?"
  ],
  "safe_through": 1153,
  "temporary_decisions": [
    "Render 블라디미르 as “Vladimir,” 흑룡공 as “Black Dragon Duke,” and 파이 첸 as “Pie Chen.”",
    "Render 외교 as “Diplomacy” for Morgoth’s distinctive use of genuine surrender offers."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 평화 | **Peace Guild** | Guild name. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 드레이크 | **Drake** | High-tier dragonkin monster. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 외눈박이 | **One-Eyed** | Epithet of Carus, who has only one eye. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 사성 | **Four Saints** | Rank the Blood Lord says Jeok Cheongang might have attained if the Great Faction War had continued another year. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 펜타곤 | **Pentagon** | Headquarters of the United States Department of Defense and source of intelligence about terrorist experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 폰허브 | **Pornhub** | Website referenced in Taekyung's joke about Jin-ho. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 한국 | **Korea** | Destination of the international Hunters and Guild Masters. |
| 흑룡공 | **Black Dragon Duke** | Title in Morgoth's System announcement. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 1153
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1152
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1136
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1148
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, and the Son of Heaven has formally enfeoffed him as Prince Shangshan.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1148
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1139
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 1150
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃1154화



망막에 비친 모든 공간이 어둡고 탁했다.

방사성 낙진마저 지워 버린 마력은 거무스름한 안개가 되어 떠돌았고, 오망성(五芒星)의 형태를 이룬 성벽은 산처럼 높았다.

그리고.

고오오옹.

그 모든 것의 중심에, 놈이 있었다.

흑룡공(黑龍公) 모르고스가.

콰아아아!

찰나를 쪼개고 쪼갠 순간 속, 거대한 흑룡이 아가리를 벌림과 동시에 터져 나온 마력의 폭발.

가장 높은 첨탑 위에서 불현듯 솟아오른 칠흑빛 기둥은 끝없이 뻗어 나갔다.

구름을 뚫고, 하늘을 반으로 가르며, 저 아득히 머나먼 달까지 닿으려는 것처럼.

아니, 어쩌면 정말로 가능할지도 모른다는 생각이 들었다.

그것은 세상에서 가장 강력한 생명체가 토해 내는 숨결이자, 분노 어린 포효였으니까.

‘드래곤 브레스(Dragon Breath)……!’

나는 입술 사이를 비집고 흘러나오려는 침음성을 가까스로 억눌렀다.

비록 영상에 불과하지만, 그 안에 담긴 떨림과 공기는 내 본능을 일깨우기에 충분했다.

다르다.

단언컨대, 지금껏 내가 보고 겪은 브레스와는 차원이 달랐다.

어느샌가 요란하게 두방망이질 치고 있는 심장과 한껏 곤두선 전신의 솜털이, 얼음장처럼 차게 느껴지는 혈관의 피가 증인이자 판사로서 알려 준다.

수년 전의 나에게 씻을 수 없는 트라우마를 안겨 주었던 외눈박이 블랙 와이번도.

마력에 의해 이성을 잃고 타락했던 동정호의 수신룡(水神龍)도.

심지어는 드래곤 하트를 자신의 것으로 만들었던 미카엘 실베르트조차도 저토록 강력한 브레스를 뿜어 내지는 못했다는 사실을.

아마도 그것은 타고난 종(種), 그 자체의 차이인 동시에 기나긴 세월과 함께 켜켜이 쌓여 온 힘의 무게일 터였다.

‘이것이, 드래곤.’

단순한 홀로그램을 넘어 현실처럼 느껴지는 그 무시무시한 힘에 나는, 아니 회의실 안의 모두는 전율할 수밖에 없었다.

도대체 ‘왜’ 놈이 텅 빈 허공을 향해 드래곤 브레스를 쏘았느냐는 근본적인 의문조차 잊은 채.

하지만 다음 순간.

화아아악.

칠흑색으로 물들어 가는 하늘을 보며 불현듯 깨달았다.

모르고스의 진짜 목적이 무엇이었는지.

쿠구구구궁.

하늘이 쪼개지는 듯한 굉음과 함께 몰려든 수많은 먹구름이 달과 별을 가리고, 이내 물감이 퍼지듯 수천 킬로미터에 달하는 모스크바의 상공을 장악했다.

마치, 세계를 분리하는 하나의 선처럼.

그리고 심연이 내려앉은 그곳은, 지금껏 인류가 상상으로만 그려 왔던 차원 너머의 또 다른 세상을 닮아 있었다.

이 모든 재앙의 근원이자 시작.

마계(魔界)를.

“……!”

“……!”

벼락이 정수리를 파고든다면 이런 기분일까.

얼어붙은 공기 속, 노이즈 낀 홀로그램 영상에 담긴 의미를 알아차린 이들은 감히 입도 열지 못한 채 눈을 부릅떴다.

그저 으스러질 듯이 주먹을 움켜쥐고, 이를 악물고, 핏발 선 눈으로 바라볼 수밖에 없었다.

동시에, 들었다.

가장 높은 첨탑(尖塔) 위에 우뚝 선 채, 칠흑빛 하늘을 향해 부르짖는 흑룡의 외침을.

- ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ!

귀가 아닌 머릿속에서 울려 퍼지는 듯한 포효.

단순한 소리를 넘어 의지에 닿아 있는 그 정체불명의 언어는 이 자리의, 아니 전 세계의 누구도 알아들을 수 없는 것이었으나 나만큼은 예외였다.

“……부름에 답하라.”

신음과도 같은 뇌까림이 흘러나온 그때.

스아아아.

태풍의 핵처럼 소용돌이치던 구름이 갈라졌다.

하늘과 땅을 떨어 울리던 굉음도, 미친 듯이 휘몰아치던 바람도 사라졌다.

일순간 모든 소음이 사라지고 공기마저 멈춘 듯한 세상은 믿을 수 없을 만큼 평화로워 보였다.

갈라진 구름의 틈새 사이로 끔찍한 재앙의 파도가 쏟아져 내리기 전까지는.

그극, 콰아아아아!

허공이 일렁였다.

아니, 찢어졌다.

그리고 샛노란 눈동자를 번뜩이는 수백, 수천 마리의 와이번과 드레이크가, 그 거대한 몸과 날개에 달라붙은 무수한 괴물들이 지상을 향해 쏟아져 내렸다.

리치(Lich)들이 동시에 마법을 시전하자 아득한 상공에서 운석처럼 내리꽂히던 대형 몬스터들이 깃털처럼 지상에 내려앉았고, 유령마를 타고 허공을 질주한 데스나이트(Death Knight)들은 각자의 군단을 통솔하여 드넓은 폐허를 메웠다.

기쁨과 살의가 뒤섞인 포효를 내지르며.

- 그아아아아!

차차창!

헤아릴 수도 없을 만큼 많은 병장기가 바람을 만난 갈대숲처럼 흔들린다.

쿵, 쿵, 쿠구궁!

하나하나가 작은 산과 같은 대형 몬스터들이 힘차게 발을 구르고, 수백 마리의 리치와 데스나이트가 무릎을 꿇었으며, 그 열 배에 달하는 용족(龍族)은 포악한 날갯짓으로 하늘을 가로질렀다.

자신들을 이 세상으로 인도해 준, 오직 한 존재를 향한 경의.

그러나 흑룡의 두 눈동자는 어느덧 서서히 닫혀 가는 구름 틈새의 게이트(Gate)도, 그 아래 군집한 수십만의 몬스터 대군도 아닌 카메라의 초점을 정확히 응시하고 있었다.

- 은빛 산의 주인이자 마계의 대공(大公)인 나, 모르고스의 영혼과 이름을 걸고 너희 인간에게 맹세하건대.

홀로그램 너머의 괴물과 시선이 맞닿은 그 순간, 나는 불현듯 깨달았다.

지금 내가 보고 있는 이 영상은 모르고스가 전 세계의 인류에게 보내는 선전포고이자 항복 권고라는 사실을.

- 저항할 시에는 그 어디에서도 본 적 없는 가장 끔찍한 종말을, 항복을 택한다면 완전한 평화와 생존을 약속할지니.

하지만.

- 만약 너희가 살아남고자 한다면, 나의 통치하에 새롭게 태어난 이 땅으로 찾아와 충성을 맹세하라.

그럼에도 불구하고.

- 그러나 모든 것에는 최소한의 대가가 따르는 법.

모든 것을 예측하지는 못했다.

- 사흘 뒤, 나는 이곳의 왕좌에 앉아 너희가 바친 공물을 영원한 약속의 증표로서 기쁘게 받아들이겠다.

모르고스가 얼마나 교활한 존재인지.

- 수십억 인간족의 목숨과는 비교할 수도 없는, 고작 두 명의 인간을.

놈의 진정한 목적이 무엇인지.

- 내 앞에 무릎 꿇려라.

흑요석을 닮은, 심연처럼 소용돌이치는 용의 눈동자가 번뜩였다.

- 천태민과, 진태경을.

그 순간.

띠링.

서늘하게 귓가를 파고드는 시스템 알림과 함께, 오직 나만이 볼 수 있는 홀로그램 창이 떠올라 눈 앞을 가렸다.



* * *



이미 인류는 여러 국제기구가 예측했던 것보다도 더, 아니 어쩌면 그 이상으로 훨씬 빠르게 안정을 되찾아가고 있었다.

모스크바가 소멸하는 영상은 모두를 충격과 공포의 구렁텅이로 밀어 넣기에 충분했으나, 채 몇 시간도 지나지 않아 공표된 한 가지 사실은 그들에게 있어 구원의 사다리와 같았다.



‘그’가 돌아왔어.

└ 세상에, 신이시여. 농담은 아니겠지?

└ 사실이야. UN공식 발표라고. 지금 당장 TV를 틀어. 모든 채널에서 방송하고 있으니까.

└ 빌어먹을, 환상적이군. 이대로 다 끝나는 줄 알았는데.

└ 도대체 어떻게 된 거야? 그가 돌아왔다니 기쁘지만, 왜 이런 상황이 된 뒤에야 나타난 거지?

└ 네가 폰허브 최우수 고객이 되는 동안 그는 전 세계를 돌아다니면서 사람들을 구했으니까. 그는 중동에서도 이미 죽을 고비를 넘겼어.

└ 진심으로 걱정돼서 하는 말인데, 이 멍청한 댓글은 지우는 게 좋을 거야. 30분쯤 뒤에 찾아온 FBI가 너희 집 문을 박살내고 그 살찐 엉덩이를 걷어차 버리기 전에.

└ 내가 무슨 잘못을 했는데? 난 아무런 잘못도 저지르지 않았어.

└ 사실 맞는 말이야. 저 불쌍한 친구는 돌고래보다 낮은 아이큐를 가진 죄밖에 없지.

└ 그래, 다들 너무 비난하지는 마. 그냥 길 가다가 마주치면 샷건이나 한 발 박아주라고.

└ 시ㅂㅏㄹ새끼가 뒤질라고.

└ 오, 한국인 친구가 왔군. 흥분해서 오타까지 낸 걸 보니 저놈은 이제 게임도 제대로 못 할 거야. 코리안들은 한번 찍은 표적을 놓치지 않지.

└ 그리고 놈에게 헤드샷을 선물한 한국인은 아마 12살쯤 되는 어린애일 테고.

└ 아무튼 중요한 건, 우리가 살았다는 거야.

└ 맞아. 그가 돌아왔으니까.



사람들은 금세 희망을 되찾았다.

모르고스가 출현한 이래, 그 흔한 농담 한마디 없이 얼어붙어 있던 인터넷 게시판에도 활기가 돌았다.

이름을 말하지 않아도 모두가 ‘그’가 누구인지 알고 있었으니까.

지금의 인류에게 있어 진태경은 그런 존재였다.

누구보다 강하고, 믿을 수 없을 만큼 헌신적이며, 그 어떤 고난이 찾아와도 극복하여 끝내 증명해 내고야 마는.

몇몇 이들은 아직도 그를 제2의 천태민이라고 칭했으나, 대부분의 의견은 달랐다.

이미 진태경은 그 어떤 미사여구가 필요하지 않은, 새로운 시대의 구원자였다.

의식불명이 된 천태민의 빈자리를 채우는 것으로도 모자라 자신의 것으로 만들었고, 전 세계 곳곳의 재앙을 수습하며 수많은 인명을 구했던 그를 누가 대신할 수 있단 말인가.

그렇기에 사람들은 안심했다.

진태경이 돌아왔으니, 흐트러져 있던 모든 것이 제자리를 찾을 것이라고.

지금껏 그래왔듯이 그가 나서서 해결해 줄 거라고.

하지만 그로부터 채 하루가 지나기도 전, 펜타곤을 비롯한 전 세계로 날아든 한 장의 경고장을 받아든 인류는 똑똑히 깨달았다.

- ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ!

사상 초유의 게이트를 넘어 지구를 침략한 저 거대한 군대 앞에서, 자신들이 잠시나마 품었던 희망이 얼마나 헛된 것이었는지.

- 그러나 모든 것에는 최소한의 대가가 따르는 법.

그리고 어느덧 괴물의 달콤한 제안에 귀를 기울이고 있는 자신들의 모습과.

- 내 앞에 무릎 꿇려라.

살고자 하는 욕망이, 인간을 어느 정도로 비겁하게 만들 수 있는지도.

- 천태민과, 진태경을.

다시 한번 전 세계가 요동쳤다. 

누군가는 분노했지만, 누군가는 굳게 입을 닫았다.

전자는 결사 항전을 부르짖었고, 후자는 비난을 피해 목소리를 숨겼다.

하지만 그로부터 다시 반나절의 시간이 흐른 뒤.

구구구궁!

마침내 러시아 전역을 장악하고, 사방으로 진격하는 몬스터 군단의 모습을 영상으로 확인한 사람들은 모두 침묵을 택할 수밖에 없었다.

차마 누구에게도 말하지 못한, 한 가지의 생각을 동시에 떠올리며.
```

## Final English reading copy

```markdown
# Chapter 1154

Everything in my field of vision was dark and murky.

The magical power that had erased even the radioactive fallout drifted about as a blackish fog, and the walls arranged in the shape of a pentagram towered like mountains.

And—

Goooooong.

At the center of it all stood that bastard.

Black Dragon Duke Morgoth.

KWAaaaaa!

In a moment split into ever smaller fractions, a gigantic black dragon opened its jaws, and an explosion of magical power burst forth.

A pitch-black pillar shot up from the highest spire and stretched endlessly onward.

Piercing the clouds, cleaving the sky in two, as if it meant to reach the distant, faraway moon.

No—maybe it really could.

It was the breath of the most powerful living creature in the world, and a roar filled with rage.

*Dragon Breath…!*

I barely managed to suppress the groan rising between my lips.

It was only a video, but the tremor and atmosphere within it were enough to awaken my instincts.

This was different.

I could say with certainty that it was on an entirely different level from any Breath I’d ever seen or experienced.

My heart was suddenly pounding wildly, the fine hairs all over my body stood on end, and the blood in my veins felt cold as ice. They bore witness and passed judgment.

The One-Eyed Black Wyvern that had left me with an indelible trauma years ago.

The Water God Dragon of Dongting Lake, corrupted and driven mad by magical power.

Even Michael Silbert, who had made a Dragon Heart his own.

None of them had ever unleashed a Breath that powerful.

Perhaps it was the difference in their very species, combined with the weight of power amassed over a long, long time.

*So this is a dragon.*

The terrifying power felt more real than a mere hologram. I couldn’t help but shudder—and neither could anyone else in the conference room.

We even forgot to ask the obvious question: *Why* had Morgoth fired a Dragon Breath into empty space?

But the next moment—

Fwaaaash.

As I watched the sky turn pitch-black, I suddenly understood Morgoth’s true purpose.

Rrrrrumble.

With a deafening roar, countless dark clouds surged in, covering the moon and stars. Then, like ink spreading through water, they took over the skies above Moscow for thousands of kilometers.

Like a single line dividing the world.

And the place where the abyss had settled resembled another world beyond our dimension, one humanity had only ever imagined.

The source and beginning of this entire calamity.

The Demon Realm.

“……”

“……”

Would this be what it felt like if lightning struck the crown of your head?

The air had frozen. Those who understood the meaning hidden in the glitching holographic footage could only stare, eyes wide, unable to speak.

They clenched their fists until they nearly broke them, gritted their teeth, and stared with bloodshot eyes.

At the same time, they heard it.

The black dragon stood tall atop the highest spire, crying out toward the pitch-black sky.

—ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ!

The roar seemed to ring out not in my ears, but inside my head.

It was more than a sound; it reached the level of will. No one here—or anywhere in the world—could understand the mysterious language.

Except me.

“……Answer the call.”

The words slipped out as a groan.

Shaaah.

The clouds, swirling like the eye of a typhoon, parted.

The deafening roar that had shaken heaven and earth faded, and so did the wind that had been raging like mad.

All noise vanished in an instant. The world, with even the air seemingly still, looked impossibly peaceful.

Until a dreadful wave of disaster poured through the gap in the clouds.

Krrrk—KWAaaaaa!

The empty space rippled.

No—it tore open.

Hundreds, thousands of Wyverns and Drakes, their yellow eyes flashing, poured toward the ground, along with countless monsters clinging to their enormous bodies and wings.

When the Liches cast their spells in unison, the giant monsters plunging down like meteors from the distant sky drifted gently to the ground like feathers. Death Knights raced through the air on ghostly horses and led their legions to fill the vast ruins.

They roared with cries that mingled joy and bloodlust.

—GRAAAAAH!

Clang! Clang!

Countless weapons swayed like a field of reeds in the wind.

Thud. Thud. Rrrrrumble!

The giant monsters, each one like a small mountain, stamped their feet. Hundreds of Liches and Death Knights went down on one knee, while ten times as many dragonkin cut through the sky with savage beats of their wings.

A display of reverence for the one being who had brought them into this world.

But the black dragon’s eyes were fixed on the camera, not on the Gate in the clouds slowly closing above, nor on the hundreds of thousands of monsters gathered beneath it.

—In the name of my soul and my name, I, Morgoth, master of the Silver Mountains and Archduke of the Demon Realm, swear to you humans:

The moment my eyes met the monster’s through the hologram, I suddenly realized something.

This video was Morgoth’s declaration of war—and his demand for humanity’s surrender.

—If you resist, I promise you the most horrific end you have ever seen. If you surrender, I promise complete peace and survival.

But—

—If you wish to survive, come to this land, reborn under my rule, and swear your loyalty.

Even so—

—But everything has its price.

There was still one thing I hadn’t predicted.

—Three days from now, I will sit upon the throne here and gladly accept the tribute you offer as a token of our eternal pact.

Just how cunning Morgoth was.

—Just two humans—a paltry price next to the lives of billions of your kind.

What his true purpose was.

—Bring them to their knees before me.

The dragon’s eyes, like swirling abysses of obsidian, flashed.

—Cheon Taemin and Jin Taekyung.

At that moment—

Ding.

A System notification pierced my ears with a chill, and a holographic window only I could see appeared, blocking my view.



* * *



Humanity was already recovering its stability faster than the various international organizations had predicted—or perhaps even faster than that.

The footage of Moscow’s destruction was enough to plunge everyone into an abyss of shock and fear. Yet a single fact announced less than a few hours later was like a ladder of salvation to them.

*He’s* back.

└ Oh my God. Please tell me this isn’t a joke.

└ It’s true. Official UN announcement. Turn on the TV right now. It’s on every channel.

└ Holy shit, that’s incredible. I thought we were all done for.

└ What the hell happened? I’m glad he’s back, but why did he only show up after things got this bad?

└ Because while you were becoming Pornhub’s best customer, he was traveling the world and saving people. He already came close to dying in the Middle East.

└ I’m genuinely worried about you, so you should delete this stupid comment before the FBI shows up in about thirty minutes, breaks down your door, and kicks your fat ass.

└ What did I do wrong? I didn’t do anything wrong.

└ He’s got a point, actually. The poor guy’s only guilty of having a lower IQ than a dolphin.

└ Yeah, don’t be too hard on him. If you happen to run into him on the street, just put a shotgun round in him.

└ You motherfukcer, you wanna die?

└ Oh, our Korean friend is here. He’s so worked up he even made a typo. That guy won’t be able to play games properly anymore. Koreans never miss the target once they’ve locked on.

└ And the Korean who gives him a headshot will probably be a kid around twelve.

└ Anyway, the important thing is that we’re alive.

└ Right. He’s back.



People quickly found hope again.

Ever since Morgoth appeared, the internet message boards had been frozen, not even managing the most ordinary joke. Now they were full of life again.

They all knew who *he* was, even without anyone saying his name.

That was what Jin Taekyung meant to humanity now.

Stronger than anyone, impossibly devoted, and able to overcome whatever hardship came his way and prove himself in the end.

Some still called him a second Cheon Taemin, but most disagreed.

Jin Taekyung had become a savior of a new age, one who needed no embellishment.

Who else could fill Cheon Taemin’s place while he lay unconscious—and make that place his own—then clean up disasters around the world and save countless lives?

That was why people felt relieved.

Jin Taekyung was back. Surely everything that had fallen into disarray would return to its proper place.

Just as he always had, he would step in and set things right.

But less than a day later, humanity received a warning from Morgoth that reached across the world, including the Pentagon. Then they understood all too well:

—ᚨᚾᛊᚹᛖᚱ ᚦᛖ ᚲᚨᛚᛚ!

How futile the hope they had briefly felt was, faced with that great army that had invaded Earth through a Gate unlike any before it.

—But everything has its price.

And how they were already listening to the monster’s sweet offer.

—Bring them to their knees before me.

How far the desire to survive could make people stoop.

—Cheon Taemin and Jin Taekyung.

Once again, the whole world was thrown into turmoil.

Some were enraged, but others kept their mouths firmly shut.

The former called for a fight to the death; the latter hid their voices to avoid criticism.

But half a day later—

Rrrrrumble!

At last, people saw footage of the monster army that had seized all of Russia and was advancing in every direction. They had no choice but to fall silent.

All thinking the same thing, though they couldn’t bring themselves to say it to anyone.
```
