<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1170.txt",
      "sha256": "c2a4b7489f85844e3fead7c65fff6cd671c96dd1abc31b7cf1fdbdb5e6e8182e",
      "bytes": 13181
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "40935d7ca1acaa5757552b1e7c435764ffefa0f4f81d3ab1fc9cc73664e90588",
      "bytes": 1000
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e5e79ce2dcef0e436ab63d6d7ce4514037a40b7300c4332ed3928f63771f12a9",
      "bytes": 248116
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4585fee4e2753db746fd368a728c2bb537fbd970190b70415b5413a00756aebe",
      "bytes": 760
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "90e13f7d47199c9d32caf684a65b58ab4bbde7356de0fdb7511c39d858ce1eed",
      "bytes": 867
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "934149478bf023f0d1400b937f9918943f8cff677910c2fc8325fbc72bfc2f7e",
      "bytes": 1516
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c92d519ebd10150573499b1ee660b70e2607e74c0aa00553f8d3d8f719d0a14a",
      "bytes": 623
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "c44430678a810ab18cbbf1c5bc0e0cdf749848e10e695b6e535a39e12b46e1bb",
      "bytes": 756
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "02105a09de1c198057348e9c6549fe936899c2bdce0a36cf85acf84fcd178483",
      "bytes": 877
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "5a8e3361cbacf0a27cb7c506c37e00d6a2d7184dc29f51ef48942212866071c8",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "97b900dbb29a57db84ee2adbffd58479c504d0863bf1805451d09b1ed9be91d4",
      "bytes": 294489
    }
  ],
  "estimated_tokens": 10266
}
-->

# Durable State Update — Chapter 1170

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
1 and safe_through 1170. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1170. Profile updates may replace only one
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
  "chapter": 1170,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1170,
    "continuity_sources": [1170],
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
    "Humanity won the battle against Morgoth; its surviving forces are wounded but rallying.",
    "Jin’s physical injuries were healed by leveling up, but severe mental exhaustion remains; his Fire Dragon Armor was destroyed.",
    "Jin created Open Heaven, the third form of the Fire Dragon Divine Spear; Fire Gate Divine Technique and Qi Sense reached the ninth star.",
    "Jin gained insight into Mind’s Eye, which activates only under certain conditions and causes extreme fatigue.",
    "Morgoth is gravely wounded and nearing death, with his Dragon Heart exposed.",
    "Morgoth spent millennia seeking God and now calls Jin chosen by God.",
    "The Skeleton King’s head appeared and spoke to Jin."
  ],
  "continuity_sources": [
    1169
  ],
  "open_questions": [
    "Is Jin truly chosen by God, and what does that mean?",
    "What will happen to Morgoth and the Skeleton King?"
  ],
  "safe_through": 1169,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 시스템              | **System**                     |
| 명성               | **Fame**                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 모르고스 | 진태경 | enemy Dragon addressing a human opponent | you | formal, measured | Uses 자네 while addressing Jin. |
| 진태경 | 모르고스 | human opponent addressing an enemy Dragon | son | casual and mocking | Calls Morgoth 아들. |
| 모르고스 | 아스모데우스 | being summoned by Asmodeus | Asmodeus | formal and measured | Morgoth directly addresses Asmodeus while reflecting on his failure. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1169
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 1159
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1169
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he masks fear with anger and protects those he cherishes, while recognizing that his enemies fear him too.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1169
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1166
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Tutorial Helper is confirmed to be the Martial God, whom Jin remembers as humanity’s savior.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1169
- **Aliases:** None
- **Role:** Morgoth is a Dragon and sovereign of a vast palace who collects powerful beings he kills or subdues as Guardians, including seven S-rank Hunters from Earth.
- **Personality:** Composed and intellectually curious, Morgoth spent millennia seeking God and treats powerful beings as trophies out of possessive desire; he can recognize and accept his own fear as a reason to grow stronger.
- **Voice:** He speaks in polished, measured phrasing, but can drop his courtesy for blunt, direct admissions when speaking sincerely.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth holds the Skeleton King as a trophy and commands seven soul-stolen S-rank Hunters as Guardians.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1168
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1170화



마침내 스켈레톤 킹을 되찾았다는 안도감도 잠시.

피에 젖은 이빨 사이로 흘러나온 용의 한마디를 들은 진태경의 눈빛이 깊숙이 가라앉았다.

“내가, 신의 선택을 받았다고?”

혼잣말처럼 새어 나온 의문에, 모르고스는 실소했다.

- 내게 묻는 것이라면, 참으로 어리석군.

“그게 무슨-”

- 진태경이여, 나는 너의 모든 것을 온전히 알지 못하기에 그저 짐작할 수밖에 없다. 설령 그 강대한 힘으로 뭇 세상을 무릎 꿇렸던 아스모데우스라 할지라도 마찬가지일 테지. 그는 전능(全能)할지언정, 전지(全知)하지 못하니.

당연했다.

전지전능은 오직 한 존재를 위한 표현이었으니까.

신.

어디에서도 볼 수 없으나, 어디에나 있는 존재.

모든 것을 알고, 모든 것을 행할 수 있는 이.

그러나 지금 모르고스는 하늘이 아닌 진태경을 바라보고 있었다.

자신이 수천 년 동안 찾아 헤맸던 신의 그림자를 망토처럼 두르고 있는 한 인간을.

- 내가 아닌 너 자신에게 물어라. 답은 그곳에 있다.

“……!”

일순간 파르르 떨리는 눈동자와 덜컥 굳어 버린 신형.

진태경은 대답하지 않았다.

아니, 대답할 수 없었다.

그저 등줄기를 타고 솟구치는 한 줄기의 전율 속, 불현듯 들이닥친 기억의 파도에 휩쓸리고 있을 뿐이었다.

‘아스모데우스는 죽었어. 내가 태어났던 그 날에, 승리의 날에.’

사막 위에 세워진 거대한 신전의 중심부, 마주한 적을 향해 과거의 진태경이 씹어뱉듯 말을 이었다.

‘놈은 소멸했고, 우리는 승리했다. 그게 전부야. 진실이고.’

입술 밖으로 흘러나오는 갈라진 목소리가 마치 남의 것처럼 낯설다.

그리고 그 모습을 보며 심연의 괴물이, 도플갱어가 미소 지었다.

‘그 말 또한 맞다. 진태경, 선택받은 자여. 그것이 너희가 알고 있는 전부이자 진실일 테니.’

선택받은 자.

도플갱어의 입을 통해 처음으로 그 낯선 단어를 들었을 때, 진태경은 알지 못했다.

그로부터 얼마 지나지 않아 생각지도 못했던 누군가에게서 그와 같은 말을 듣게 될 줄은.

‘너였구나.’

반란군의 피와 시체로 뒤덮인 황궁의 대연회장 위, 마침내 정체를 드러낸 궁성(弓星)이 말을 이었다.

‘무신(武神)께서 말씀하셨던, 선택받은 자가.’

그래.

이번이 처음이 아니었다.

도플갱어와 궁성이, 그런 그녀에게 서신을 남긴 무신이.

심지어는 시스템까지도 그를 선택받은 자라 칭했다.

도플갱어를 소멸시킨 바로 그 날에.



[당신은 선택받은 자, 방주의 주인]



짧았던 그 한 줄의 시스템 메시지를 떠올리며, 진태경은 모르고스를 바라보았다.

정확히는, 용의 거대한 눈동자에 비친 자신의 모습을.

“그래. 네 말이 맞아.”

피로에 젖은 육신과 달리 그 어느 때보다 선명하게 빛나는 안광(眼光).

진태경은 스스로에게 속삭이듯 말을 이었다.

“나는…… 이미 답을 알고 있었을지도 모르지.”

늘 생각했었다.

어느 날 손에 넣은 이 놀라운 이능(異能)이 도대체 어디에서, 또한 누구로부터 비롯된 것인지.

다만 끊임없이 부정하고 의심했을 뿐이다.

왜 하필 자신이었는지.

많고 많은 수십억 인류 중, 어찌하여 보잘것없는 F급 헌터가 선택받은 것인지.

정말 그처럼 전지전능한 신이 존재한다면, 어째서 지금껏 벌어진 그 무수한 참극과 재앙을 직접 막아서지 않았는지.

그러나 모르고스의 되물음을 듣는 순간 깨달았다.

자신이 이토록 선명한 진실을 눈앞에 두고도 외면해 왔던 이유를.

“버거웠다. 매 순간 내가 짊어진 모든 것이.”

아버지의 이른 죽음, 남겨진 가족, 누군가의 희생을 발판 삼아 이어 나가야 하는 삶.

형태는 달랐으나, 무게는 같았다.

그리고 그 하나하나가, 태산처럼 한 인간의 몸과 마음을 짓눌렀다.

“아마도 그 때문이었겠지. 신을 원망하게 된 이유가.”

- 원망한다고?

생각지도 못한 대답을 들은 모르고스가 피가래 끓는 소리를 내며 웃었다.

- 재미있군. 그 누구보다 그분께 감사해야 할 네가?

“그러기에는 너무 많은 걸 잃었으니까. 그것도 아주 소중한 것들을.”

- 얻은 것 역시 있었겠지. 그 또한 소중했을 테고.

“맞아. 소중한 만큼 더 무겁지. 이제는 정말 견딜 수 없을 정도로.”

- 정말 그렇게 생각하나?

“넌 나를 잘 몰라. 인간에 대해서는 더더욱.”

- 아니, 잘 알고 있다. 어쩌면 너희들 중 그 누구보다도.

담담한 대답과 함께, 모르고스는 노을빛에 잠겨 가는 세상을 바라보았다.

- 분명 이곳은 다르다. 내가 태어나고 자란 세상과 너무나도 큰 차이가 있지.

당연했다.

지구라 불리는 이 낯선 세상에는 세 개의 달과 태양도, 열두 개의 대륙과 아홉 바다도 존재하지 않았으니까.

그뿐인가.

모든 것이 마법으로 세워지고 이루어진 대도시와 정령이 살아 숨 쉬는 총천연색의 대자연도.

이러한 세상 곳곳에서 각자의 영역을 지키며 살아가는 여러 종족도 없었다.

만약 대격변이라는 재앙을 통해 크나큰 변화를 겪지 않았다면, 그 차이는 더욱 극명하게 두드려졌을 것이다.

- 하지만 단 한 가지, 예외가 있더군. 설령 아스모데우스가 이 세상을 침공하지 않았더라도 그것만큼은 달라지지 않았을 거야.

다음 순간 모르고스가 무엇을 말하려는지, 진태경은 불현듯 깨달았다.

“인간.”

- 그래. 너희 인간들이다. 내가 보고 겪은 모든 종족 중 가장 나약하고 어리석은 존재들. 하여 참으로 희한했다.

진태경을 똑바로 응시하며, 모르고스가 덧붙였다.

- 내가 오래전 떠나왔던 그곳에서도, 세상의 지배자는 언제나 인간이었다는 사실이.

“……!”

- 처음에는 좀처럼 이해할 수 없더군. 너희의 수명과 지혜는 요정을 따라갈 수 없고, 난쟁이들처럼 뛰어난 신체 능력을 지닌 것도, 하다못해 몬스터와 같은 번식력을 갖추지도 못했으니까.

하지만 모르고스의 고향에서도 인간은 번성했다.

그들이 이룩한 문명은 드래곤을 제외한 그 어떤 종족도 따라올 수 없을 만큼 눈부셨고, 뛰어난 마법사와 기사들의 명성은 바다를 넘어 전 대륙을 뒤흔들었다.

모르고스가 모든 면에서 가장 뒤떨어졌다고 생각한 종족이 한 세상의 패권을 틀어쥔 것이다.

그리고 어느 때보다 길었던 탐구와 유희 끝에, 그는 마침내 답을 찾아낼 수 있었다.

- 욕망. 너희 인간은 끝없는 욕망으로 이루어진 존재다. 그렇기에 계속해서 변화하지.

답은 찾았지만, 이해는 할 수 없었다.

인간이란 그토록 복잡한 생물이었다.

힘이 약하면 약속이라도 한 듯 뭉치고, 그 크기가 커지면 갈라서기를 반복한다.

충분히 많은 것을 얻었음에도 그들은 계속해서 싸웠다.

아름다운 요정들을 노예로 사로잡기 위해.

금은보화가 잠든 난쟁이들의 광산을 강탈하기 위해.

몬스터들의 부산물로 마법을 연구하고 더욱 날카롭고 단단한 무구를 만들기 위해.

심지어는 같은 동족을 죽이고 그 영토를 빼앗기 위하여 인간들은 싸웠다.

살아남기 위해 싸우는 것이 아니라, 더욱 큰 무언가를 얻기 위해 피를 흘리고 목숨을 잃었다.

욕망이 탐욕으로 변질된 것이다.

- 하지만 모든 인간이 그런 것은 아니었다. 몬스터보다도 추악한 본능에 사로잡힌 자가 있었다면, 그 반대도 있었지.

흑요석처럼 번뜩이던 눈빛은 이미 본래의 빛을 잃은 지 오래.

모르고스는 서서히 흐릿해져 가는 시선으로 진태경을 바라보았다.

- 바로 너처럼.

“……무슨 말을 하고 싶은 거냐.”

- 너 또한 인간이다. 그렇기에 마음속 깊이 자리 잡은 욕망이 존재하고, 분명 그 욕망을 채우기 위해 계속해서 변화했겠지. 그것을 원했든, 원치 않았던 말이다.

“그건.”

진태경은 문득 입을 다물었다.

모르고스의 말은 모두 사실이었으니까.

처음에는 단순히 강해지고 싶었다.

자신에게 주어진 한계를 벗어나고, 이를 말미암아 더욱 많은 돈과 유명세를 얻어 자랑스러운 아들이자 오빠가 되고 싶었다.

그런데 문득 정신을 차려보니, 모든 것이 뒤바뀌어 있었다.

불과 이 년 전에는 상상한 적도, 할 수도 없었던 막대한 책임감의 무게도 함께.

‘그렇다면, 나는 이걸 어떻게 지금까지 버틸 수 있었던 거지?’

답은 이번에도 가까이에 있었다.

‘나 역시 변화한 거야. 갈수록 무거워지는 책임감을 견딜 수 있을 만큼. 계속해서.’

그리고 세상은 그것을 변화가 아닌 다른 이름으로 부른다.

성장(成長).

이루었고, 이어지고 있다.

아이가 소년이, 소년이 청년이 되고 어느새 온 인류의 앞길을 밝힐 횃불이자 새로운 구원자가 된 것처럼.

그렇기에 진태경이 마음속 깊은 곳에 품은 것은 가장 순수한 욕망이자, 동시에 욕망이라는 단어를 넘어선 무언가였다.

“희망(希望).”

그 순간, 모르고스는 느낄 수 있었다.

바짝 메마른 입술 사이로 흘러나온 두 글자에 담긴 힘을, 반짝이는 생기를.

- 희망이라, 그게 네가 찾아낸 답인가?

진태경이 고개를 저었다.

“그렇게 생각했는데, 아니더라고.”

- 그럼?

“잠시 잊고 있던 거였어. 매번 숨 막히는 상황에서 발버둥 치는 것만으로도 벅찼으니까.”

말 그대로였다.

찾아낸 것이 아니다. 기억해 낸 것이다.

언제부턴가 잊고 있던 감정을.

모든 이가 자신을 바라보며 희망을 떠올리고 있음에도, 정작 진태경은 단 한 순간도 마음 편한 적이 없었다.

그는 횃불이니까.

가장 앞에서, 가장 짙은 어둠과 홀로 싸우며 나아가야 했으니까.

하지만 이제는 아니다.

진태경은 그 어느 때보다 간절히 희망했다. 소원하고, 기원했다.

지금 이 순간에도 자신의 이름을 부르짖으며 싸우고 있는 저들과 함께 마지막까지 살아남기를.

그리고 이 빌어먹을 이야기가 부디 해피 엔딩으로 장식되기를.

“사실 누구에게 선택받았건, 설령 그게 망상이나 착각이었다고 해도 상관없어.”

진태경은 창대를 지팡이 삼아 지친 몸을 일으켜 세웠다.

“나는 해 왔고, 해낼 거다.”

스릉.

흔들림 없는 주인의 의지처럼, 변함없는 예기(銳氣)를 간직한 창날이 노을빛을 받아 번뜩인다.

“하나만 묻자.”

- 허락한다.

“이유가 뭐지?”

질문은 짧았으나, 모르고스는 그 말에 담긴 뜻을 알고 있었다.

지금 진태경은 묻고 있었다.

왜 스켈레톤 킹을 그토록 순순히 내주었는지.

지난 수천 년의 삶을 끊어 낼 자신에게 어째서 이런 말과 행동을 보이는지.

하지만 모르고스에게 있어 이는 너무나도 당연하면서도 쉬운 질문이었다.

- 네가 조금이라도 더 강해질 수 있다면, 앞으로의 일이 더욱 재미있어질 테니까.

“뭐?”

굳은 얼굴로 반문하는 진태경의 모습에 모르고스는 소리 내어 웃었다.

죽음을 앞에 두고도 끝끝내 포기하지 못한 유희에 대한 갈망과 스스로를 향한 자조를 섞어서.

‘그래, 아스모데우스여. 이제야 알겠군. 왜 그대가 나를 이 세상으로 불러들였는지.’

너무나도 늦게 깨닫게 되었지만, 이것으로 충분하다.

정해진 섭리를 벗어난 존재를 보았고, 신의 선택을 받은 인간 또한 확인했으니.

그리고.

‘목에 걸고 있는 저건…… 분명해. 틀림없다.’

모르고스는 똑똑히 보았다.

갈기갈기 찢겨 나간 진태경의 옷 사이로 언뜻 드러난 한 가지 물건을.

동시에 선명하게 느낄 수 있었다.

마나도, 마력도 아닌 신비로운 기운이 그것을 빈틈없이 감싸고 있음을.

‘다행이군. 이렇게라도 그분의 흔적을 확인할 수 있어서.’

마음속에서 공허하게 흩어지는 뇌까림과 함께, 모르고스는 마지막 힘을 쥐어 짜내어 입을 열었다.

- 자, 이제 새로운 유희를 시작해 볼까.

그 순간.

슈확!

용의 심장을 향해 쏘아지는 한 줄기의 섬광을 따라, 눈부신 노을빛이 산산이 부서졌다.
```

## Final English reading copy

```markdown
# Chapter 1170

The relief of finally getting the Skeleton King back lasted only a moment.

Jin Taekyung’s eyes sank as he heard the Dragon’s words spill between bloodied teeth.

“I was chosen by God?”

Morgoth gave a dry laugh at the question that escaped like a mutter.

“If you’re asking me, that’s foolish.”

“What does that—”

“Jin Taekyung, I cannot know all there is to know about you. I can only guess. Even Asmodeus, who brought countless worlds to their knees with his immense power, would be no different. He may be omnipotent, but he is not omniscient.”

Of course.

Omniscient and omnipotent were words meant for only one being.

God.

A being nowhere to be seen, yet present everywhere.

One who knew all things and could do all things.

But now, Morgoth was looking not at the sky, but at Jin Taekyung.

At a human wearing the shadow of the God he had spent thousands of years searching for like a cloak.

“Ask yourself, not me. The answer is there.”

“……!”

His eyes trembled. His body stiffened.

Jin Taekyung gave no answer.

No—he couldn’t answer.

He was swept away by a wave of memories that came crashing in without warning, amid a single shiver racing up his spine.

*Asmodeus is dead. On the day I was born. The day of our victory.*

At the heart of the enormous temple built atop the desert, the Jin Taekyung of the past spoke through gritted teeth to the enemy before him.

*He was erased, and we won. That’s all. That’s the truth.*

The hoarse voice coming from his lips sounded unfamiliar, as if it belonged to someone else.

Watching him, the monster of the abyss—the Doppelganger—smiled.

*That is also true, Jin Taekyung, chosen one. It must be all you know, and the truth as you understand it.*

Chosen one.

When Jin Taekyung first heard that strange phrase from the Doppelganger, he had no idea that before long, he would hear the same words from someone he never expected.

*So it was you.*

In the imperial palace’s grand banquet hall, covered in the rebels’ blood and corpses, the Bow Saint finally revealed her identity and spoke.

*The chosen one the Martial God spoke of.*

Right.

This wasn’t the first time.

The Doppelganger. The Bow Saint. The Martial God, who had left her a letter.

Even the System had called him the chosen one.

On the very day he erased the Doppelganger.

> **System**
>
> You are the chosen one, Master of the Ark.

Remembering that brief line of System text, Jin Taekyung looked at Morgoth.

More precisely, at his own reflection in the Dragon’s enormous eye.

“You’re right.”

Unlike his body, soaked in exhaustion, his eyes shone more clearly than ever.

Jin Taekyung continued, as if whispering to himself.

“Maybe… I already knew the answer.”

He’d always wondered.

Where had this incredible power he’d suddenly gained come from? And who had given it to him?

But he’d done nothing but deny and doubt it.

Why him?

Of all the billions of people in the world, why had an insignificant F-rank Hunter been chosen?

If a God as omniscient and omnipotent as that truly existed, why hadn’t He personally stopped the countless tragedies and disasters that had happened?

But the instant he heard Morgoth’s question, he understood why he had kept turning away from the truth, even when it was right in front of him.

“It was too much. Everything I had to carry, every moment.”

His father’s untimely death. The family he left behind. A life that could continue only by standing on someone else’s sacrifice.

The burdens took different forms, but weighed the same.

And each one pressed down on a person’s body and mind like a mountain.

“Maybe that’s why I came to resent God.”

“Resent Him?”

Morgoth laughed, his voice thick with bloody phlegm, at the unexpected answer.

“Interesting. You, who should be more grateful to Him than anyone?”

“I’ve lost too much for that. Things that mattered more than anything.”

“You gained things, too. They must have mattered just as much.”

“Yeah. The more they matter, the heavier they are. Now they’re almost too much to bear.”

“Do you really think so?”

“You don’t know me. You know even less about humans.”

“No. I know them well. Perhaps better than anyone among you.”

With that calm reply, Morgoth looked out at the world sinking into the colors of sunset.

“This place is certainly different. It’s nothing like the world where I was born and raised.”

Of course it was.

This strange world called Earth had neither three moons and a sun, nor twelve continents and nine seas.

And that wasn’t all.

There were no great cities built and run entirely by magic, no brilliantly colored natural landscapes teeming with spirits.

Nor were there different races living across the world, each protecting its own territory.

If the disaster called the Great Cataclysm hadn’t brought such enormous changes, the contrast would have been even more striking.

“But I found one exception. Even if Asmodeus had never invaded this world, this one thing would have remained the same.”

Jin Taekyung suddenly realized what Morgoth was about to say.

“Humans.”

“Yes. You humans. The weakest and most foolish beings among all the races I’ve seen and known. That was what I found so strange.”

Looking straight at Jin Taekyung, Morgoth added,

“Even in the world I left long ago, humans were always the rulers.”

“……!”

“At first, I couldn’t understand it. Your lifespans and wisdom couldn’t match the elves. You weren’t physically gifted like the dwarves, and you didn’t even have the reproductive capacity of monsters.”

And yet, humans had thrived in Morgoth’s homeland.

The civilization they built was so brilliant that no race except the Dragons could match it. The fame of their extraordinary mages and knights had crossed the seas and shaken every continent.

The race Morgoth thought inferior in every way had seized dominion over a world.

And after a long period of study and amusement, longer than ever before, he finally found an answer.

“Desire. You humans are made of endless desire. That’s why you keep changing.”

He had found the answer, but he couldn’t understand it.

Humans were such complicated creatures.

When they were weak, they banded together as if they’d made a pact. When their numbers grew, they split apart again and again.

Even after gaining more than enough, they continued to fight.

To capture beautiful elves and enslave them.

To plunder the dwarves’ mines, where gold and treasure lay.

To use monster parts to study Magic and make weapons sharper and stronger.

They even fought to kill their own kind and take their land.

They didn’t fight to survive. They bled and died to get something more.

Their desire had turned into greed.

“But not all humans were like that. If some were ruled by instincts uglier than a monster’s, there were others at the opposite extreme.”

The eyes that had once glinted like obsidian had long since lost their light.

Morgoth looked at Jin Taekyung through a gaze that was slowly growing dim.

“Like you.”

“……What are you trying to say?”

“You’re human, too. So you have desires rooted deep in your heart, and you must have kept changing to fulfill them, whether you wanted to or not.”

“That’s—”

Jin Taekyung suddenly fell silent.

Everything Morgoth said was true.

At first, he’d simply wanted to get stronger.

To break free of the limits imposed on him, and through that, gain more money and fame—and become a son and older brother his family could be proud of.

But when he came to his senses, everything had changed.

And with it came the weight of an enormous responsibility he had never imagined—and could never have imagined—just two years earlier.

*Then how have I managed to bear all this until now?*

The answer was close at hand this time, too.

*I changed, too. Enough to bear the responsibility as it kept getting heavier. I kept changing.*

And the world called that something else. Not change.

Growth.

He had grown, and he was still growing.

A child had become a boy, a boy had become a young man—and before he knew it, a torch lighting the way for all humanity, a new savior.

That was why what Jin Taekyung held deep in his heart was the purest of desires, and at the same time, something beyond the word desire.

“Hope.”

In that moment, Morgoth could feel it.

The power and bright vitality in the word that had passed through those parched lips.

“Hope. Is that the answer you found?”

Jin Taekyung shook his head.

“That’s what I thought. But it wasn’t.”

“Then?”

“I’d just forgotten. I was so overwhelmed, just struggling through one suffocating moment after another.”

That was exactly it.

He hadn’t found it. He had remembered.

A feeling he’d forgotten somewhere along the way.

Even though everyone looked at him and thought of hope, Jin Taekyung himself hadn’t felt at ease for a single moment.

Because he was a torch.

He had to press forward alone at the very front, fighting the deepest darkness.

But not anymore.

Jin Taekyung hoped more fervently than ever. He wished, he prayed.

That he would survive to the end alongside those who were fighting even now, shouting his name.

And that this goddamn story would, please, have a happy ending.

“Honestly, I don’t care who chose me. Even if it was all a delusion or a misunderstanding.”

Using his spear as a cane, Jin Taekyung pushed himself to his feet.

“I’ve made it this far, and I’ll see it through.”

*Shing.*

Like the unwavering will of its master, the spearhead retained its keen edge and flashed in the sunset.

“I have one question.”

“I’ll allow it.”

“Why?”

The question was brief, but Morgoth understood what lay behind it.

Jin Taekyung was asking why he had so readily given up the Skeleton King.

Why he would say these things and act this way toward the one who was about to end his life of thousands of years.

But to Morgoth, the answer was obvious—and simple.

“If you can become even a little stronger, then what comes next will be more interesting.”

“What?”

At Jin Taekyung’s stiff-faced reply, Morgoth laughed aloud.

His laughter held both a longing for amusement that he could not quite give up, even in the face of death, and self-mockery.

*Yes, Asmodeus. Now I understand why you summoned me to this world.*

He had realized it far too late, but this was enough.

He had seen a being who stood outside the ordained order, and confirmed the existence of a human chosen by God.

And—

*That thing around his neck… It can only be. I’m certain.*

Morgoth had seen it clearly.

One object, glimpsed through Jin Taekyung’s clothes, torn to shreds.

At the same time, he could feel it clearly.

A mysterious energy, neither mana nor magical power, enveloped it completely.

*How fortunate. At least I could confirm a trace of that person.*

With those words fading emptily in his heart, Morgoth summoned the last of his strength and opened his mouth.

“Now, shall we begin a new amusement?”

In that instant—

*Shwaa!*

The dazzling sunset shattered into pieces, following the streak of light shooting toward the Dragon Heart.
```
