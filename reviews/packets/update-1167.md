<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1167.txt",
      "sha256": "06737e46cb18c1cc6b35db2d2bd10d1db9ae294e0c7c3d6607f56c28adff5da8",
      "bytes": 11534
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "cfc2f0c35ee62d1d2c879a0cf9401fe5a36493c2d4a28be140f353b0a35fea5b",
      "bytes": 875
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "629c127707aeb33bfd33dddf3e4142c30166c25d518472a55ae7f7af5cf583ca",
      "bytes": 247860
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "94922bbfec7cfd8b1334f1906001806d781ba915535234de3cadc6c873a9405d",
      "bytes": 779
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5f900ffcd2f0cab9d962db42579e46e98498dc3cc48bee46126361e13afa2cf1",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "4f6a2a9802b4ddbc4addcc35661820728be7bd2c6a7b56cb927b29e19bd96116",
      "bytes": 545
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "09c19549753df58629facb0f5040a72f31f504fc6e53b7c44d943541dbb02d70",
      "bytes": 1642
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f942b2e3f220ba7b46313503ebedbdf8429ae516ec2197cf3fcdabfd052224c3",
      "bytes": 623
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "63133a4dfaaac8f32211516f4de698207009b6008c903391c6b2b8f6179e1d6e",
      "bytes": 841
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "62ba55f278563f620fc6fb8989c72424c2d0d19c16ab375085711986c60ac4df",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "97b900dbb29a57db84ee2adbffd58479c504d0863bf1805451d09b1ed9be91d4",
      "bytes": 294489
    }
  ],
  "estimated_tokens": 9357
}
-->

# Durable State Update — Chapter 1167

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
1 and safe_through 1167. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1167. Profile updates may replace only one
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
  "chapter": 1167,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1167,
    "continuity_sources": [1167],
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
    "Morgoth has bound Jin after Jin expended his remaining strength and fired Dragon Breath at him.",
    "Jin’s fate after the Dragon Breath is unresolved.",
    "Jin’s Fire Dragon Divine Spear reached Great Completion, and Trance was applied as he entered No-self.",
    "Jin perceives the world through the Mind’s Eye and has lifted his spear.",
    "Morgoth recognizes his fear of Jin and says he will grow stronger by accepting it.",
    "The Tutorial Helper, Martial God, and humanity’s savior are the same remembered figure."
  ],
  "continuity_sources": [
    1165,
    1166
  ],
  "open_questions": [
    "Did Jin survive Morgoth’s Dragon Breath, and can he counterattack?",
    "What will Jin perceive or do through the Mind’s Eye while in No-self?"
  ],
  "safe_through": 1166,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 초식     | **form**                                         | Numbered technique movement                           |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 무아지경 | **Trance** | State Taekyung briefly enters during the energy digestion. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 황하 | **Yellow River** | River along which civilization began. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 무아 | **No-self** | The brief self-forgetting state the disciple mistakes for a breakthrough. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 모르고스 | 진태경 | enemy Dragon addressing a human opponent | you | formal, measured | Uses 자네 while addressing Jin. |
| 진태경 | 모르고스 | human opponent addressing an enemy Dragon | son | casual and mocking | Calls Morgoth 아들. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 1161
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1166
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1165
- **Aliases:** None
- **Role:** Magic Johnson is the United States' Grand Mage and a War Mage, one of the two remaining masters of Magic.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** He speaks casually and directly, with colloquial phrasing and occasional profanity.
- **Relationships:** He is Jin Taekyung's friend.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1166
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he masks fear with anger and protects those he cherishes, while recognizing that his enemies fear him too.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; seven of his allies’ old S-rank Hunter comrades are Morgoth’s soul-stolen Guardians, whom the arriving Hunters now fight.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1166
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1166
- **Aliases:** None
- **Role:** Morgoth is a Dragon and sovereign of a vast palace who collects powerful beings he kills or subdues as Guardians, including seven S-rank Hunters from Earth.
- **Personality:** Composed and intellectually curious, he treats powerful beings as trophies out of possessive desire, but can recognize and accept his own fear as a reason to grow stronger.
- **Voice:** He speaks in polished, measured phrasing, but can drop his courtesy for blunt, direct admissions when speaking sincerely.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth holds the Skeleton King as a trophy and commands seven soul-stolen S-rank Hunters as Guardians.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1163
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1167화



그것은 단순한 찌르기가 아니었다.

정확히는, 공격과 방어라는 개념에서 벗어난 무언가에 가까웠다.

‘왜 그래야 하지?’

몽롱한 의식 사이로 불현듯 떠오른 의문과 함께, 진태경은 어느덧 검푸른 화염이 깃들어 있는 백염의 창날을 비스듬히 올려 세웠다.

허공을 뒤덮으며 쏟아져 내리는 용의 숨결을 향해.

마치 살 없는 우산으로 폭포를 막으려 하는 어리석은 이처럼.

스륵.

초식(招式)이라 부를 수도 없을 만큼 간단한 움직임.

하지만 다음 순간 그 미세한 변화가 불러일으킨 결과는, 미증유의 힘과 지식을 지닌 고룡조차도 예상치 못했던 것이었다.

콰아아아아!

일순간 부풀어 오르는 동공.

마침내 되돌아온 가파른 시간의 흐름 속, 모르고스는 자신도 모르게 눈을 부릅떴다.

‘이게 무슨……!’

갈라진다.

직경만 수 미터에 달하는 거대한 마력의 기둥이, 창날과 맞닿음과 동시에 수십 갈래로 나뉘어 갈라지고 있었다.

지금 이 순간조차도.

‘도대체 어떻게?’

지금껏 수천 년의 세월을 살았다.

때로는 인간으로, 요정과 난쟁이로, 혹은 몬스터의 거죽을 뒤집어쓴 채 강자만이 누릴 수 있는 유희를 즐겼고 무수한 경험과 지식을 손에 넣었다.

그렇기에 모르고스는 더더욱 이해할 수 없었다.

어찌하여 이와 같은 현상이 가능한 것인지.

자신의 발톱보다도 작은 한 인간이, 어떻게 드래곤 브레스에 담긴 기운의 결을 읽어 낼 수 있는 것인지.

그러나 이와 같은 모르고스의 의문은 그저 공허한 메아리에 지나지 않았다.

무아지경(無我之境)에 휩싸인 진태경 자신조차 그 의문에 제대로 대답할 수 없었으니.

아니, 스스로가 무엇을 하고 있는지조차 모를 만큼 그의 의식은 깊고도 먼 어딘가에 머무르고 있었다.

단지 보이는 대로 행할 뿐.

구구구구궁!

어둡다. 온 사방이 칠흑빛이다.

먹먹한 굉음이 귓가를 울리고, 창날을 따라 상하좌우로 빗겨져 나간 마력은 본의 아니게 하나의 둥그런 막이 되어 진태경의 몸 주위에만 머물렀다.

적어도, 다른 시선에서 보이는 모습은 그랬다.

스아아아.

어째서일까.

밝다. 환하다.

이미 세상 전체가 어둠에 잠긴 듯 캄캄한데, 어느샌가 검푸른 빛을 띤 진태경의 두 눈으로 전해지는 시야는 무수한 빛으로 번뜩이고 있었다.

‘아름답다.’

진태경은 시야를 가득 채운 형형색색의 빛줄기를 바라보았다.

어떤 것은 붉고, 어떤 것은 푸르다.

눈이 부실 만큼 순백의 색을 띤 것이 있는 반면, 깊이를 알 수 없을 정도로 순수한 어둠을 간직한 것 역시도 있었다.

바로 지금, 브레스보다 한 걸음 늦게 들이닥친 수십 종류의 마법이 그랬다.

물, 불, 얼음, 돌풍, 벼락.

하나하나가 능히 천 단위의 목숨을 앗아 갈 만큼 강대한 위력을 품은 그것들은 오직 단 한 사람을 이 세상에서 지우기 위해 발현된 것이었고, 진태경은 그 사실에 감사했다.

만약 저 마법들이 자신이 아닌 아군을 향한 것이었다면, 그들은 처참한 죽음을 피할 수 없을 테니까.

‘인벤토리 오픈, 소환.’

모든 것이 한순간이었다.

낡은 철창이 불현듯 허공에 나타난 것도, 그와 동시에 진태경이 본능에 따라 중단전(中丹田)의 기운을 끌어올린 것도.

슈확!

그것은 쾌속하면서도 강맹했다.

중단전의 힘을 개방한 이후 그 어느 때보다도.

그리고 타오르는 화염을 머금은 채, 한 줄기의 벼락이 되어 공간을 가로지른 철창은 궤적에 있는 모든 마법의 핵(核)을 관통한 후에야 모든 힘을 소진했다.

꽈아아아아앙!

하늘이, 땅이 뒤흔들린다.

목표에 닿지 못하고 폭발한 마법들이 화려하게 허공을 수놓고, 그 믿을 수 없는 광경을 목격한 흑룡은 그 거대한 아가리를 크게 벌렸다.

드래곤 하트에 잠재된 막대한 마력을 한층 강하게 끌어올리며.

콰아아아!

창날을 통해 전해지는 엄청난 압력.

바로 그때였다.

더욱 강하게, 동시에 끊임없이 쏟아지는 용의 숨결 아래에서 진태경이 지면 깊숙이 박혀 있던 무릎을 일으켜 세운 것은.

‘일어나야 해.’

머릿속을 가득 채운 단 하나의 생각.

가야 했다. 갈 수밖에 없었다.

그렇기에 지금만큼은 모든 것을 잊을 수 있었다.

뼈마디가 어긋나는 고통도.

지금 당장이라도 창날과 함께 자신의 몸뚱어리를 집어삼킬 것만 같은 저 끔찍한 마력의 결정체도.

전신을 옥죄이는 가시넝쿨과 두 어깨를 짓누르는 막대한 중력(重力)도.

콰직!

마치 어린아이가 태어나 처음으로 내딛는 첫걸음처럼 위태롭게 앞으로 나아간 발걸음.

하지만 지면에 새겨진 발자국의 깊이처럼, 그 안에 담긴 진태경의 힘과 의지는 그 어느 때보다 무겁고 강인했다.

한낱 마법 따위로는 막을 수 없을 정도로.

우드득!

쇠사슬처럼 전신을 휘감고 있던 가시넝쿨이 찢겨 나가고, 만근 거석과도 같았던 중력이 옅어진다.

콰직.

한 걸음.

콰직.

또 한 걸음.

느리지만 망설임 없이, 진태경은 나아갔다.

꿈결에 휩싸인 듯 흐릿하게 물든 두 눈에 비치고 있는 거대한 그림자를 향해, 칠흑빛 브레스의 중심에서 홀로 빛나는 창날을 횃불로 삼아서.

그리고 그런 진태경의 등 뒤에는, 그를 위해서라면 기꺼이 위험을 무릅쓸 수 있는 동료가 있었다.

“지옥의 겁화가 우리의 적을 불사를지니-”

흡사 포효와도 같은 대마도사의 외침이 굉음 사이로 울려 퍼진 그때.

화아아악!

일순간 붉게 물든 하늘 너머, 먹구름 사이로 모습을 드러낸 십여 개의 화염구가 흑룡의 머리 위를 향해 겨누어졌다.

“헬 파이어(Hell Fire)!”

구구궁!

마침내 완성된 스펠과 함께 창공을 살라 먹으며 들이닥치는 맹렬한 열기.

하지만 이 갑작스러운 공격 앞에서도 모르고스는 조금도 당황하지 않았다.

아니, 자신을 향한 것이 칼날도 아닌 마법이라는 사실에 되려 분노 어린 비웃음을 머금었다.

그는 다른 누구도 아닌 드래곤.

경이 속에서 탄생한 마법의 주종(主種)이자, 심지어 한때 가장 높은 곳에서 모든 동족을 이끌었던 드래곤 로드.

‘사라져라.’

소리 내어 뱉을 필요조차 없었다.

모르고스에게는 강력한 의지와 그보다 더한 마력이 있었고, 그의 마법은 인간을 포함한 그 어떤 종족도 닿을 수 없는 아득한 영역에 존재했으니.

퍼어어엉!

안티 매직(Anti magic).

드래곤의 마력이 인간의 마나를 집어삼킨다.

잿가루와 불씨가 뒤섞여 흩날리고, 저 멀리 가디언들과의 일전 도중 위험을 감수하고 나선 매직 존슨이 피를 토하며 무릎을 꿇었다.

마나 역류.

마법사로서 겪을 수 있는 가장 치명적인 부상.

그러나 붉은 핏물에 흠뻑 적셔진 대마도사의 입가는 어느덧 부드러운 호선을 그리고 있었다.

그가 만들어 낸 이 찰나의 빈틈으로 인해, 또 다른 누군가는 아주 잠시나마 중력으로부터 자유로워질 수 있었으니까.

“어서 가, 진.”

달싹이는 입술 사이로 희미한 목소리가 흘러나온 그 순간.

화륵.

진태경이 내디딘 발끝을 따라 화염이 솟구쳤다.

일순간 느슨해진 중력을 이겨내고, 반경 수십 미터를 감싼 마법의 범위를 벗어나기에 충분한 힘을 지닌 열기가.

콰아아앙!

기운의 압축과 폭발.

그리고.

쇄도(殺到).

쐐애애액!

하나의 선처럼 이어지고 있는 드래곤 브레스를 베어 가르며 진태경은 질주했다.

가까워지는 거리만큼, 동시에 모르고스가 느끼는 위험만큼 지상을 향해 쏟아져 내리는 용의 숨결은 거칠고 강해졌으나 상관없었다.

아니, 오히려 거칠어진 만큼 더욱 선명해진 힘의 흐름을 따라 나아갔다.

사방을 뒤덮은 무수한 굉음과 비명을 뒤로한 채.

단 한 치의 망설임도 없이 계속해서 앞으로, 또 앞으로.

그리고 마침내 태산처럼 드리워진 용의 거대한 그림자가 가까워졌을 때, 진태경은 자신이 무엇을 해야 하는지 본능적으로 깨달았다.

화룡신창 이 초식.

천격(天格).

콰아아아!

그것은 이 자리의 그 누구도 본 적 없는 경이로운 광경이었다.

검푸른 화염에 휩싸인 창날이, 거대한 어둠의 기둥을 반으로 가르며 솟아올랐다.

하늘을 향해 날아오르는 한 마리의 용처럼.

화룡(火龍) 그 자체가 되어.



* * *



모든 것은 찰나의 순간에 시작되고, 끝났다.

파아아앗!

어둠이, 마침내 힘을 다한 용의 숨결이 흩어진다.

다른 누구도 아닌 한 인간에 의해서.

그리고 이 믿을 수 없는 광경을 바라보며, 모르고스는 문득 생각했다.

도대체 어디서부터 잘못된 것인지.

그의 마음 깊숙이 자리 잡은 오만과 방심이, 이리도 큰 눈덩이가 되어 덮쳐 올 만큼 잘못된 것이었는지.

혹은.

불과 백년 남짓의 수명을 지닌 어느 필멸자의 힘과 의지가, 자신을 뛰어넘을 만큼 강했던 것인지.

‘아니, 그럴 리 없다.’

그의 이름은 모르고스.

드높은 은빛 산의 주인이자, 마계의 대공.

느려진 세상 속에서 홀로 뇌까린 태고의 흑룡은 거대한 두 날개를 폈다.

그리고 창공을 가르며 다시 한번 솟구쳐 오르는 자그마한 신형을 향해 내리꽂혔다.

퍼어어엉!

압축된 공기가 폭발한다.

하늘에서 지상으로.

지상에서 하늘로 향하는 두 개의 그림자가 서로를 향해 쏘아진다.

칠흑빛 마력에 휘감긴 용의 발톱이, 검푸른 화염이 담긴 창날이 공간을 찢어발기며 나아간다.

오직 이 순간만을 위해 살아왔던 것처럼.

- 나는, 나는……!

휘몰아치는 바람 너머, 모르고스는 맹렬한 부르짖음과 함께 자신의 모든 것을 실어 거대한 발톱을 내리그었다.

동시에, 불현듯 깨달았다.

자신이 지금 휘두른 이 앞발이, 이미 다른 누군가로 인해 베어져 있었다는 것을.

그리고 그 상처는 본체로 되돌아온 지금까지도 사라지지 않았다는 사실을.

‘스켈레톤 킹.’

얕지만, 치유되지 않았던 한 줄기의 상처.

누군가에게는 전리품에 불과했으나, 다른 누군가에게는 친구였던 그가 남긴 마지막 집념의 흔적이 바로 지금 생각난 것은 모르고스의 본능적인 직감일지도 몰랐다.

어쩌면.

정말로 어쩌면.

지난 수천 년간의 기나긴 유희가, 마침내 막을 내릴지도 모른다는 직감.

그리고 불길한 직감은 언제나 빗나가는 법이 없었다.

서걱.

낮고도 예리한 한 줄기의 절삭음.

주인의 의지가 깃든 창날이, 친구의 마지막 흔적을 파고들었다.
```

## Final English reading copy

```markdown
# Chapter 1167

It wasn’t a simple thrust.

More precisely, it was something that had slipped beyond the concepts of attack and defense.

*Why should it have to be?*

As the question surfaced amid his hazy consciousness, Jin Taekyung had already tilted the White Flame’s spearhead, wreathed in blue-black fire, upward.

Toward the Dragon’s Breath pouring down to blanket the sky.

Like a fool trying to stop a waterfall with an umbrella that had no fabric.

*Shh.*

A movement so simple it could hardly be called a form.

But the result of that tiny change, in the very next instant, was something even an Ancient Dragon with unprecedented power and knowledge could never have predicted.

*Rrrrrumble!*

Morgoth’s pupils widened in an instant.

As time’s rapid flow finally returned, the Black Dragon’s eyes flew open before he even realized it.

*What is this…?!*

It was splitting apart.

A massive pillar of magical power, several meters in diameter, was splitting into dozens of streams the moment it touched the spearhead.

Even now.

*How is that possible?*

He had lived for thousands of years.

At times as a human, an elf, or a dwarf; at others wearing the hide of a monster. He had enjoyed the amusements only the strong could afford, and gained countless experiences and knowledge.

That was precisely why Morgoth found this all the harder to understand.

How could such a phenomenon be possible?

How could a human smaller than his claw read the flow of energy in Dragon Breath?

But Morgoth’s questions were nothing more than empty echoes.

Even Jin Taekyung, lost in Trance, couldn’t properly answer them.

No—his consciousness had wandered so far away that he didn’t even know what he was doing.

He simply did what he saw.

*Rrrrrumble!*

Dark. Pitch-black in every direction.

A muffled roar filled his ears. The magical power deflected up, down, left, and right along the spearhead had, unintentionally, formed a rounded barrier around Jin Taekyung alone.

At least, that was how it looked to anyone else.

*Fwoooosh.*

Why?

It was bright. Radiant.

The whole world was already swallowed in darkness, yet the view reaching Jin Taekyung’s eyes, now glowing blue-black, glittered with countless lights.

*Beautiful.*

Jin Taekyung gazed at the strands of color filling his vision.

Some were red, others blue.

Some shone a dazzling white, while others held a pure darkness of unfathomable depth.

The dozens of kinds of Magic that arrived a step behind the Breath were just like that.

Water, fire, ice, gusts of wind, lightning.

Each held enough power to take a thousand lives. They had been unleashed for the sole purpose of erasing one person from this world, and Jin Taekyung was grateful for it.

If those spells had been aimed at his allies instead of him, they would have suffered a horrible death.

*Inventory open. Summon.*

It all happened in an instant.

The old iron spear suddenly appeared in midair. At the same time, Jin Taekyung instinctively drew up the energy in his Middle Dantian.

*Fwoosh!*

It was swift and powerful.

More so than at any point since he had unlocked the power of his Middle Dantian.

The iron spear, carrying a blaze and streaking through space like a bolt of lightning, pierced the core of every spell in its path before its power finally ran out.

*KABOOOOOM!*

The sky and the earth shook.

The spells, which had exploded before reaching their target, painted the sky in a dazzling display. Witnessing the unbelievable sight, the Black Dragon opened his enormous jaws wide.

He drew even more power from the vast magical force dormant within his Dragonheart.

*Rrrrrumble!*

An immense pressure came through the spearhead.

That was when Jin Taekyung lifted the knee he had driven deep into the ground, beneath the Dragon’s Breath raining down harder and harder without pause.

*I have to get up.*

One thought filled his mind.

He had to go. He had no choice but to go.

And so, just this once, he could forget everything.

The pain of his bones grinding out of place.

The horrifying mass of magical power, ready to swallow his body along with the spearhead at any moment.

The thorny vines constricting his entire body, and the immense gravity pressing down on both shoulders.

*Crack!*

He took a step forward, unsteady as a child’s first step.

But like the deep footprint he left behind, the strength and will within Jin Taekyung were heavier and stronger than ever.

No mere Magic could stop him.

*Crack!*

The thorny vines wrapped around his body like chains tore apart, and the gravity that had weighed as much as a massive boulder began to weaken.

*Crack.*

One step.

*Crack.*

Another step.

Slowly, but without hesitation, Jin Taekyung moved forward.

Toward the enormous shadow blurred in his dreamlike vision, using the spearhead that shone alone at the center of the pitch-black Breath as a torch.

And behind him stood a comrade willing to brave any danger for his sake.

“May the flames of hell consume our enemies—”

Just then, the Grand Mage’s cry, like a roar, rang out amid the din.

*Fwoooosh!*

Against the suddenly reddened sky, a dozen or so fireballs emerged from the storm clouds and took aim at the Black Dragon’s head.

“Hell Fire!”

*Rrrrrumble!*

The spell was complete. A fierce heat rushed in, scorching the sky.

But Morgoth wasn’t even slightly startled by this sudden attack.

No—he wore an enraged sneer at the thought that what was coming for him was Magic, not a blade.

He was no one but a Dragon.

The master species of Magic, born of wonder—and a Dragon Lord who had once led all his kind from the highest place of all.

*Disappear.*

He didn’t even need to say it aloud.

Morgoth had a powerful will and even greater magical power. His Magic existed in a distant realm no other race, humans included, could ever reach.

*PAAAM!*

Anti Magic.

The Dragon’s magical power devoured the humans’ mana.

Ash and embers swirled through the air. Far away, Magic Johnson—who had risked intervening in the middle of his fight with the Guardians—coughed up blood and dropped to his knees.

Mana Backlash.

The most devastating injury a mage could suffer.

And yet, the Grand Mage’s mouth, drenched in blood, had curved into a gentle smile.

Because the brief opening he had created gave someone else a chance, even if only for a moment, to escape the gravity.

“Go, Jin.”

At that moment, a faint voice slipped between his barely moving lips.

*Fwoosh.*

Flames surged from the tip of Jin Taekyung’s foot as it touched down.

Heat strong enough to overcome the momentarily weakened gravity and carry him beyond the range of the Magic surrounding a radius of dozens of meters.

*KABOOM!*

Compressed energy and an explosion.

And then—

A charge.

*Whooooosh!*

Cutting through the Dragon Breath, which stretched ahead like a single line, Jin Taekyung raced forward.

The closer he got—and the more danger Morgoth felt—the rougher and more powerful the Dragon’s Breath pouring toward the ground became. But it didn’t matter.

If anything, the rougher it grew, the more clearly he could follow the flow of its power.

Leaving behind the countless roars and screams blanketing the battlefield.

Without a single moment’s hesitation, he kept going. Forward, and farther forward.

And at last, as the Dragon’s enormous shadow loomed over him like a mountain, Jin Taekyung instinctively realized what he had to do.

Fire Dragon Divine Spear, Second Form.

Heavenly Strike.

*Rrrrrumble!*

It was a wondrous sight no one there had ever seen.

The spearhead, wreathed in blue-black flames, rose as it cleaved through the colossal pillar of darkness.

Like a dragon soaring into the sky.

Becoming the fire dragon itself.

* * *

Everything began and ended in the blink of an eye.

*Fwoooosh!*

The darkness—the Dragon’s Breath, finally spent—dispersed.

By the hand of no one but a human.

Watching that unbelievable sight, Morgoth suddenly wondered where it had all gone wrong.

Had the arrogance and complacency deep within his heart really grown into such a massive snowball that it could come crashing down on him like this?

Or—

Had the strength and will of a mortal with a lifespan of barely a hundred years truly surpassed his own?

*No. That can’t be.*

His name was Morgoth.

Master of the lofty Silver Mountain, and Archduke of the Demon Realm.

Alone in the slowed world, the ancient Black Dragon muttered to himself and spread his enormous wings.

Then he dove toward the small figure shooting skyward once more, cutting through the heavens.

*PAAAM!*

Compressed air exploded.

From sky to ground.

From ground to sky.

Two shadows shot toward each other.

The Dragon’s claw, wrapped in pitch-black magical power, and the spearhead filled with blue-black fire tore through space as they advanced.

As if they had lived for this moment alone.

“I—I…!”

Beyond the howling wind, Morgoth let out a fierce cry and put everything he had into a slash of his massive claw.

At the same time, he suddenly realized:

The foreleg he had just swung had already been cut by someone else.

And that wound still hadn’t healed—not even now, after he had returned to his true form.

*The Skeleton King.*

A shallow wound, but one that had never healed.

To some, he had been no more than a trophy. To someone else, he had been a friend. Perhaps it was Morgoth’s instinct that made him remember, at that very moment, the final trace of the Skeleton King’s stubborn resolve.

Perhaps.

Just perhaps.

The long game he had played for thousands of years might finally be coming to an end.

And ominous instincts were never wrong.

*Shhk.*

A low, keen sound of something being sliced.

The spearhead, imbued with its wielder’s will, bit into the last trace his friend had left behind.
```
