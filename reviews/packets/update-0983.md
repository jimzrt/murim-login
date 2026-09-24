<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0983.txt",
      "sha256": "aa59acae27082db6965eda50b281c02ef325a557fc837113b0198af063b68cf7",
      "bytes": 14726
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "49a64d94a88f4b277a9968513712a94d0f1a00396038d98cdf7f82861061fe57",
      "bytes": 817
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1bd8ea740a0339a3d96d0df04fd391965026833fb4015b8cb7ff2632867c2981",
      "bytes": 236041
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1cb809c7ba02815a038eb7dfb509094bcb830d0583fb30ff49048fffb4ef6e99",
      "bytes": 759
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "c219a3bb9b7b691ad306afd9a8578d26730f98184213845f067cef2213a86064",
      "bytes": 699
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1a77f5a9d7d5c8f517913fa0f14be0083a911d05d03b0fa29f4ca1152b0ccd78",
      "bytes": 1479
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "72c5c12fcfb37d2a94b79c7242aead5135797d40dd40a772917bf77c794190ac",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "a047a186ebea9185a5361b7bef485d4f5f3781fda0cf555e72838183f8a3efa2",
      "bytes": 699
    },
    {
      "path": "characters/Murong Baek.md",
      "sha256": "4fca74a229e77907cc4704deaad6e4ed4e4845ebe5e746f3b4cd14728251aa19",
      "bytes": 660
    },
    {
      "path": "characters/Namho.md",
      "sha256": "75381ed3b9f949958da13c829c040b26e8a015d295fe1ead69c1c220bf4b2c96",
      "bytes": 973
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "acabe0bc25da8678df22c8beed7964b0f2d0636cbd45cafac49d40970c6b971d",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c2ab951f1caa3b27a1001691c8891a98f2ae89636f6b7bad11472538daeab5bb",
      "bytes": 272314
    }
  ],
  "estimated_tokens": 11952
}
-->

# Durable State Update — Chapter 983

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
1 and safe_through 983. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 983. Profile updates may replace only one
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
  "chapter": 983,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 983,
    "continuity_sources": [983],
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
    "The Murong Family has been annihilated, but Murong Yeonghwi and several dozen survivors escaped and are being pursued toward Liaoning.",
    "Jeong Hogun is leading the Embroidered Uniform Guard to Liaoning under Jin Taekyung’s order as Marquis of Shangshan.",
    "Temur is compelled to help hunt the Murong survivors; if his betrayal is exposed, his own tribespeople may kill him.",
    "Jin Wikyung is recovering from the Shanxi battle under pressure from those around him to rest."
  ],
  "continuity_sources": [
    982
  ],
  "open_questions": [
    "Will the Murong survivors, including Murong Yeonghwi, be captured in Liaoning?",
    "What threat, if any, remains after the Murong Family’s defeat?"
  ],
  "safe_through": 982,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 태원     | **Taiyuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천하오대세가 | **Five Great Families** | Expanded source form of 오대세가. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 칠공 | **seven apertures** | The seven bodily openings through which Taekyung's overflowing heat escapes. |
| 황하 | **Yellow River** | River along which civilization began. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 요녕성 | **Liaoning Province** | Province ruled by the Murong Family. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 진태경 | 모용백 | adversaries | you | informal and confrontational | Directly asks whether Murong Baek beat up his older brother. |
| 모용백 | 진태경 | adversaries | you | informal | Addresses Taekyung directly during their confrontation. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 982
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 982
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 981
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 981
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 982
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Murong Baek.md

# Murong Baek (모용백)

- **Safe through:** Chapter 982
- **Aliases:** North Heaven Demon Lord, Divine Spear of the Imugi
- **Role:** Murong Baek was the North Heaven Demon Lord, known as the Divine Spear of the Imugi; Jin Taekyung killed him after he burned his life to gain power.
- **Personality:** He coveted the dragon pearl and the chance to become a dragon, rationalizing his pursuit while choosing to seize what belonged to others.
- **Voice:** Not established
- **Relationships:** Jeok Cheongang and the Bow Saint fought him alongside Jin Taekyung, who delivered the killing blow.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 943
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 975
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃983화



정호군이 이끄는 일천의 금의위가 하북을 넘어 요녕성에 다다랐을 때는, 이미 일대의 무림인들은 물론 양민들마저 모든 진실을 알고 있었다.

유목민들의 침략. 모용세가의 배신.

마지막으로 그 배후에 도사리고 있던 암천(暗天)의 존재까지도.

그렇기에 그 어떤 혈기 넘치는 무림인조차 감히 금의위의 앞길을 가로막지 못했다.

가장 큰 이유는 두 가지였다.

첫 번째로는 대국 제일의 정예라 할 수 있는 금의위의 무력과 권위였고, 두 번째로는 황실의 깃발과 함께 나란히 휘날리는 또 하나의 깃발 때문이었다.

무림맹(武林盟).

무림의 일은 무림인들이 해결해야 한다며 목소리를 높였던 어느 명망 높은 노강호도, 우뚝 선 무림맹의 깃발 앞에서는 조용히 수긍할 수밖에 없었다.

작금의 천하를 조율하는 두 거대 세력이 뜻을 합친 이상, 남은 것은 모용세가에 대한 치죄(治罪)뿐이었으므로.

그리고 이내 모두의 이목은 한 곳을 향해 집중되었다.

요녕성 심양(遼寧).

한때 한 자루의 돌격창과 각궁으로 대륙을 질타하며 일국을 세웠던.

그러나 이제는 패망의 운명만을 앞둔 모용세가의 본가를 향해서.

“포위하라.”

두두두두!

정호군의 짧은 명령에 지축이 흔들렸다.

일천의 금의위가 나설 필요조차 없었다.

얼마 전 천자가 친히 임명했다는 상산후(上山侯)의 권위는 북방 전역을 아우를 만큼 거대했고, 나는 새도 떨어트린다는 금의위의 등장에 버선발로 마중 나온 요녕성의 성주는 즉각 자신이 가진 모든 군권(軍權)을 내놓았으니.

쿵. 쿵. 쿵.

가장 먼저 뛰쳐나간 일천의 기마대가 모용세가의 장원을 포위하고, 중무장을 갖춘 보병들이 방패와 창칼로 그 틈새를 촘촘하게 메운다.

마지막으로 궁수들이 진형을 갖추자 모든 준비가 끝났다.

여느 변방의 무림세가가 그렇듯, 천혜의 요새와도 같은 모용세가의 장원이 그렇게 빈틈없이 봉쇄된 순간이었다.

구구구궁.

육중한 마찰음과 함께 서서히 열리기 시작하는 철문.

그 너머로 눈처럼 새하얀 백의(白衣)를 걸친 사내가 모습을 드러내자, 정호군이 입을 열었다.

“발시(發矢).”

한 치의 망설임도 없는 명령.

진형을 갖춤과 동시에 만반의 준비를 끝마치고 있던 궁수들이 해야 할 일은 이미 정해져 있었다.

솨아아악!

일순간 하늘의 일부가 새카맣게 물들었다. 허공을 가르며 맹렬하게 떨어져 내리는 수백여 대의 화살 앞에서, 백의의 사내는 황급히 검을 휘둘렀다.

따다다당!

강철과 강철이 만나 불똥이 튀었다.

한 차례 철문 주변을 휩쓴 화살비가 지나간 자리에는, 낭패한 기색이 역력한 사내와 그런 그를 향한 안타까운 외침만이 남아있었다.

“공자!”

“안 됩니다! 돌아오십시오!”

“무엇하느냐! 어서 공자를 모셔 오……!”

슥.

대답 대신 단호하게 손을 내저은 사내는 입술을 깨물었다. 그리고 저 멀리 보이는 정호군을 똑바로 응시하며, 무거운 발걸음을 뗐다.

저벅.

사내의 모습을 물끄러미 지켜보던 정호군이 재차 입을 뗐다.

“발시.”

다시 한번 화살비가 쏟아지고, 검신이 번뜩였다.

다만 앞의 상황과 다른 점이 있다면, 그것은 지면에 점점이 흩뿌려진 누군가의 핏물뿐이었다.

투두둑.

화살이 박힌 어깻죽지가 잘게 경련한다. 그러나 사내의 발걸음은 멈추지 않고 계속해서 앞으로 나아갔다.

세 번째로 쏟아진 화살비 중 일부가, 그의 전신 곳곳을 파고들 때까지.

푸푹!

마침내 사내의 무릎이 꺾였다. 새하얗던 백의는 어느새 붉게 물든 지 오래였다.

그러나 더는 참지 못하고 철문 밖으로 뛰쳐나오는 가솔들을 향한 그의 외침에는 조금의 고통도 묻어나오지 않았다.

“그만! 모두 명령을 잊었는가!”

“하, 하지만……!”

“더는 나서지 마라, 무슨 일이 벌어지더라도 결코 경거망동해서는 안 될 것이다!”

철문을 넘어 달려오려던 가솔들이 이를 악물며 멈춰 섰다.

그 모습에 작게 고개를 끄덕인 사내는 검을 지팡이 삼아 비틀거리며 일어섰다.

그리고 마침내, 천천히 말을 몰아 다가오는 정호군과 마주할 수 있었다.

“이제야 뵙게 되는군요. 목숨을 걸 만한 가치가 있었던 모양입니다.”

정호군은 말안장 위에서 조용히 사내를 내려다보았다.

이렇게 가까이서 보니, 사내는 이제 겨우 약관이나 되었을 법한 용모의 청년이었다.

“모용가의 핏줄인가.”

“그렇습니다. 제 아비가 용서받지 못할 잘못을 저질렀지요.”

피는 못 속인다고 했던가.

유독 이국적인 용모를 지닌 청년을 보며 정호군은 문득 떠올렸다.

팔천협을 둘러싼 치열한 전투가 끝난 직후, 시신을 수습하는 과정에서 보았던 누군가의 얼굴을.

“그렇다면, 모용백의?”

“늘그막에 얻은 일곱째입니다. 죄 많은 아비를 둔.”

담담하게 대답한 청년이 포권을 취했다.

“모용세가의 칠공자, 모용수가 정 천호(千戶)께 인사 올립니다.”

“나를 알고 있었군.”

“저 역시 눈과 귀가 있으니, 오고 계신다는 소식은 익히 들어 알고 있었습니다.”

“그럼에도 이곳에 남아 있던 이유는?”

“제 형님들처럼 도망치면 역적(逆賊)이요, 무림공적(武林公敵)임을 스스로 시인하는 것이기 때문입니다.”

“남아 있다 한들 달라지는 것은 없다. 그래도 두 번째 이유는 들어 보도록 하지.”

청년, 모용수가 포권지례를 풀고 고개를 들었다.

정호군을 향한 눈빛은 맑았고, 뒤이어 흘러나온 목소리는 침착했다.

“누군가는 책임을 져야 하지 않겠습니까.”

“……책임이라.”

“이제 본가에 남아 있는 직계는 오직 저뿐입니다. 연관이 있는 이들은 이미 모두 죽거나 도망쳤지요.”

깊게 눌러쓴 투구 아래, 말없이 모용수를 내려다보던 정호군의 시선이 그의 어깨너머를 향했다.

“그렇다면 너와 함께 남아 있는 저들은 무엇이냐.”

“믿으실지는 모르겠으나, 저들 역시 제 아비에게 배반당한 이들입니다. 더불어 모용가의 핏줄이라 부를 만한 이들도 아니지요.”

모용수의 그 대답에, 정호군은 남아 있던 자들의 신분을 얼핏 짐작할 수 있었다.

진실에 근접할 수도 없을 만큼 가문 내에서 소외받았던 자들.

방계 중의 방계거나, 혹은 심성 자체가 맞지 않았던 이들.

더불어 아예 피 한 방울 섞이지 않은 채로 모용세가의 일부로 녹아든 빈객(賓客) 출신의 인물들이 틀림없을 터였다.

단 한 사람만 빼고.

“너 역시 아비의 만행을 몰랐더냐?”

“아는 것도, 모르는 것도 아니었습니다. 단지 어렴풋이 불길함을 느끼고 있었을 뿐.”

“그래서?”

“그저 멀리서 지켜만 보았습니다.”

“혈육의 정이라는 건가.”

“오랑캐 어미를 둔 천출(賤出)에 무재 또한 보잘 것 없는 제가 언제부터 모용가의 일원이었는지는 모르겠지만…….”

모용수가 씁쓸하게 웃으며 말을 이었다.

“한 가지만큼은 확실히 압니다. 남아 있는 이들을 구명하는 것만이 제가 할 수 있는 최선이라는 것을.”

“결국 남은 것은 너뿐이라는 이야기군. 모용백의 아들 모용수. 역적의 핏줄.”

“맞습니다. 그러니 저를 제외한 다른 이들은…….”

“즉참(卽斬)이다.”

단호하게 말을 끊어 낸 정호군의 한 마디에, 모용수의 얼굴에서 핏기가 빠져나갔다.

“그게 무슨.”

“모용세가의 가주 모용백과 그 일가는 외적(外敵)과 결탁하여 대국의 질서를 어지럽히고, 북방 일대에 막심한 피해를 입혔다. 이는 명백한 반역이며 치죄하는 것에 있어 일말의 자비도 보일 수 없다.”

“천호!”

쥐어짜듯 토해 낸 외침 속에 핏물이 뒤섞인다.

콰득, 전신 곳곳에 박힌 화살을 부러트린 모용수의 얼굴은 형용할 수 없는 참담함으로 물들어 있었다.

“말하지 않았습니까! 저들은, 저들은……!”

쿨럭.

미처 끝맺어지지 못한 말과 함께, 핏물을 뿜어낸 모용수가 무릎을 꿇은 그때.

멀리서 그 광경을 빠짐없이 지켜보고 있던 가솔들이 마침내 참지 못하고 철문 밖으로 뛰쳐나왔다.

“공자!”

“아니 되오! 공자는 죄가 없소!”

애타는 부르짖음과 함께 달려오는 그들의 모습에, 정호군은 천천히 손을 들어 올렸다.

부릅떠진 모용수의 눈동자에 팽팽하게 시위를 당기는 수백여 명의 궁수들이 비쳤다.

이제 남은 선택지는 없었다.

작은 손짓. 혹은 짧은 명령 한 마디.

그것으로 끝날 것이다. 모든 것이.

“아, 안 돼! 제발 멈추시오!”

그리고 모용수가 검붉은 핏물과 함께 간절한 외침을 토해 낸 그 순간이었다.

정호군의 등 뒤에서 늙수그레한 목소리가 들려온 것은.

“본래 인간이란 목숨이 위태로워질 때 비로소 완전한 진심을 드러내는 법이지. 자네도 그렇게 생각하지 않나. 금의위 천호 나으리?”

왜소한 체구의 노인이었다.

피부는 거무스름했고, 특이점이 돋보이는 이목구비는 한인과는 거리가 멀었다.

그러나 노인이 유독 별나 보이는 이유는, 그가 말이나 나귀가 아닌 사람을 타고 있다는 점이었다.

마치 곰과도 비교할 수 있을 것 같은 거한(巨漢)을.

“태산이. 무슨 말인지 알아들을 수 없다. 남호 혹시 노망났나?”

“씨부럴 놈. 또 시작이구먼.”

노인, 남호는 당황하지 않았다.

기다렸다는 듯이 품에서 꺼낸 육포 덩어리를 태산의 입에 쑤셔 박은 그는, 정호군을 향해 눈짓했다.

“여하튼. 노부가 보기에는 이쯤 했으면 당장으로서는 충분하지 싶은데…… 어찌 생각하나?”

잠시 생각하던 정호군이 손을 내렸다.

천천히 풀어지는 그의 손끝을 따라, 팽팽하게 당겨져 있던 수백의 활시위도 조용히 내려갔다.

“우선 관아로 압송하겠소. 남은 이들에 대한 처우는 충분한 심문을 거친 후에 결정하도록 하지.”

“그러도록 하시게. 뭐 나 같은 늙은이가 그런 것까지 막을 힘은 없지. 그 정도만 해도 저들에게는 감지덕지고.”

어깨를 으쓱해 보인 남호가 태산의 정수리를 탁탁 두드렸다.

커다란 덩치가 자세를 낮추자, 상황을 파악하지 못하고 눈만 깜빡이고 있던 모용수와 남호의 시선이 얼추 맞닿을 수 있었다.

“모용수라고 했더냐.”

“그, 그렇습니다만. 노인장께서는 대체 뉘신지.”

“나 같은 늙은이 이름까지 알 건 없고, 무림맹 소속이라는 것만 알아 두거라.”

“무림맹……!”

“아, 하나 더. 지금은 열화신룡, 아니 상산후(上山后)의 대리인이기도 하지.”

어느덧 석상처럼 딱딱하게 굳은 모용수의 얼굴을 보며 남호가 씁쓸하게 웃었다.

“그리 볼 것 없다. 단지 기회를 주고자 할 뿐이니.”

“기회……라고 하셨습니까.”

“그래, 정도(正道)에서 벗어나지 않은 이들을 위한 기회.”

남호는 알고 있었다.

아니, 진태경은 알고 있었다.

짙은 어둠 속에도 빛은 있고, 휘황한 빛줄기 속에도 어둠은 존재한다는 것을.

그것이야말로 진태경이 남호를 이곳으로 보낸 이유였다.

후환(後患)을 없애는 방법은 제거뿐만이 아니니까.

그곳에 남아 있는 것이 병 든 초목이 아니라, 튼튼하고 푸른 새싹이라면 뿌리 뽑을 이유는 없으니까.



‘정파라면, 최소한의 이름값은 해야 하는 것 아니겠습니까.’



태원진가를 떠나기 전, 진태경이 건넨 말을 떠올린 남호는 흐릿하게 웃었다.

그리고 모용수를 향해, 고작 일백 명밖에 남지 않았음에도 숨 가쁘게 달려온 그들 전부를 향해 입을 열었다.

“지금 이 순간부터, 모용세가는 존재하지 않는다.”

“……!”

“인의를 저버리고 정도를 벗어난 그들은 무림맹에 속한 정파일 수도, 세가(世家)일 수도 없을 것인즉.”

왜소한 체구가 믿어지지 않을 만큼 힘 있는 목소리는, 단 한줌의 공력도 실려있지 않았음에도 모두의 귓가를 선명하게 파고들었다.

“하나, 아직 바른길을 걷는 이가 있다면 무림맹은 그를 내치지 않을 것이다. 그것이야말로 올바른 일이므로.”

남호는 모용수를 똑바로 응시하며 말을 이었다.

“앞서 말했듯이 모용세가는 이제 존재하지 않는다. 그러나 모용가(慕容家)는 다를 것이다.”

그 혼자만의 독단이 아니다.

이는 북방의 모든 문파가, 무림맹이 결정한 사안이었다.

“추후 그대들의 결백함이 밝혀진다면, 모용가는 새로운 가주 아래에서 다시 한번 스스로를 증명할 수 있을 것이다.”

“……!”

“……!”

그 순간, 일백여 명의 가솔들은 전율에 몸을 떨었다.

모든 것이 끝났다고 생각했던 자신들에게 주어진 마지막 기회.

결백을 밝히고, 증명할 수 있는 기회가 주어졌다.

마지막까지 그들을 버리지 않았던 한 사람의 희생과 용기로.

“공자!”

모용세가가 아닌, 모용가의 가솔이 된 그들의 격앙된 음성과 눈빛이 모용수를 감싸 안았다.

머지않아 가주라 부르게 될 그를 향해.

그리고 그 광경을 잔잔한 눈빛으로 바라보던 남호는, 문득 잊고 있던 한 가지 사실을 떠올리며 작게 미소지었다.

천하오대세가(天下五代世家).

구파일방과 함께 광활한 구주 천하를 지탱하는 열다섯 개의 기둥.

모용의 성이 사라진 그 다섯 번째 빈 자리를, 누가 채울지 그는 이미 알고 있었다.

아니, 천하 무림 모두가.
```

## Final English reading copy

```markdown
# Chapter 983

By the time the thousand Embroidered Uniform Guards led by Jeong Hogun crossed Hebei and reached Liaoning Province, not only the martial artists in the region but even the common people knew the whole truth.

The nomads’ invasion. The Murong Family’s betrayal.

And, finally, the existence of Dark Heaven lurking behind it all.

For that reason, not even the most hot-blooded martial artists dared stand in the Embroidered Uniform Guard’s way.

There were two main reasons.

The first was the force and authority of the Embroidered Uniform Guard, one of the Great Nation’s finest elite forces. The second was another banner flying alongside the imperial flag.

The Murim Alliance.

Even a renowned veteran of the martial world who had loudly insisted that martial artists should handle Murim affairs themselves would have had no choice but to accept it quietly before the Murim Alliance’s towering banner.

Now that the two great powers guiding the world had joined forces, all that remained was to punish the Murong Family.

Before long, everyone’s attention focused on one place.

Shenyang, Liaoning Province.

The home of the Murong Family, which had once founded a nation after thundering across the continent with a single charging spear and a composite bow.

Now, it stood on the brink of ruin.

“Surround it.”

Thud-thud-thud-thud!

Jeong Hogun’s terse command shook the earth.

There was no need for all thousand Embroidered Uniform Guards to take action.

The authority of the Marquis of Shangshan, personally appointed by the Son of Heaven not long ago, was vast enough to encompass the entire northern frontier. And when the Embroidered Uniform Guard—the force said to knock birds from the sky—arrived, Liaoning Province’s City Lord had rushed out to greet them and immediately handed over every military force at his disposal.

Thud. Thud. Thud.

The first thousand cavalrymen galloped out to surround the Murong Family estate. Heavily armored infantry filled every gap with shields, spears, and swords.

Finally, the archers took their positions. Everything was ready.

Like any Murim family on the frontier, the Murong Family estate was a fortress made by nature itself. And now it was sealed off without a single gap.

Grrrrrr.

With a heavy grinding sound, the iron gate slowly began to open.

A man dressed in white as snow appeared beyond it. Jeong Hogun spoke.

“Loose.”

The order came without the slightest hesitation.

The archers, already in formation and prepared for this moment, knew what to do.

Fwoosh!

For an instant, part of the sky turned black. Hundreds of arrows cut through the air and fell with deadly force. The man in white frantically swung his sword in front of them.

Clang-clang-clang!

Steel met steel, sparks flying.

When the storm of arrows swept past the gate, all that remained was the man, his face stricken, and the anguished cries of those calling out to him.

“Young Master!”

“You mustn’t! Please, come back!”

“What are you doing? Bring the Young Master back—!”

The man firmly waved them back instead of answering. He bit his lip, fixed his gaze on Jeong Hogun in the distance, and took a heavy step forward.

Step.

Jeong Hogun watched him in silence, then spoke again.

“Loose.”

Once more, a rain of arrows fell, and the blade flashed.

But this time, there was one difference: blood was now spattered across the ground.

Thud-thud.

The shoulder pierced by an arrow began to twitch. But the man’s steps didn’t stop. He continued forward until some of the arrows in the third volley pierced his body.

Thwack!

At last, the man’s knees buckled. His once-white clothes had long since turned red.

Still, when the members of the family could no longer bear it and rushed out through the gate, his shout held not the slightest trace of pain.

“Stop! Have you all forgotten my orders?”

“B-but—!”

“Don’t come any closer. No matter what happens, you must not act rashly!”

The family members who had started to run through the gate clenched their teeth and stopped.

The man gave a small nod, then used his sword as a cane to stagger back to his feet.

At last, he faced Jeong Hogun, who was slowly riding toward him.

“We finally meet. I suppose it was worth risking my life.”

Jeong Hogun looked down at him quietly from the saddle.

Up close, the man was a young man who looked barely twenty.

“Are you of the Murong bloodline?”

“I am. My father committed a crime that cannot be forgiven.”

They said blood could not lie.

Looking at the young man’s distinctly foreign features, Jeong Hogun suddenly recalled a face he had seen while collecting the dead, just after the fierce battle around Eight Spring Gorge had ended.

“Then, are you Murong Baek’s…?”

“I was his seventh son, born in his old age. The son of a sinful father.”

The young man answered calmly and cupped his hands in greeting.

“I am Murong Su, the Murong Family’s Seventh Young Master. I greet Thousand Captain Jeong.”

“You know who I am.”

“I have eyes and ears of my own. I heard you were coming, of course.”

“Then why did you stay here?”

“If I fled like my elder brothers, I would be admitting with my own actions that I was a traitor and an enemy of the Murim world.”

“Nothing will change just because you stayed. Still, let’s hear your second reason.”

The young man, Murong Su, lowered his hands and lifted his head.

His gaze at Jeong Hogun was clear, and his voice was calm.

“Someone has to take responsibility, don’t they?”

“…Responsibility.”

“I’m the only direct descendant left at the family estate. Everyone connected to the crime has either died or fled.”

Beneath his deeply pulled-down helmet, Jeong Hogun silently looked at Murong Su. Then his gaze shifted past the young man’s shoulder.

“Then who are those people who stayed with you?”

“I don’t know if you’ll believe me, but they, too, were betrayed by my father. And they aren’t people who could really be called members of the Murong bloodline.”

From Murong Su’s answer, Jeong Hogun could guess the identities of the people who had stayed behind.

People so excluded within the family that they could not have come close to the truth.

They must have been distant branches of the family, or people whose temperaments simply hadn’t fit with the rest.

And among them were surely former guests who had become part of the Murong Family without sharing a drop of its blood.

With only one exception.

“Did you not know about your father’s crimes, either?”

“I neither knew nor didn’t know. I only had a vague sense that something was wrong.”

“And?”

“I simply watched from a distance.”

“Was it your affection for your own blood?”

“I don’t know when I became a member of the Murong Family, seeing as I’m the son of a barbarian mother, born of low status, with little martial talent to speak of…”

Murong Su continued with a bitter smile.

“But there’s one thing I know for sure. The best I can do is save the people who remain.”

“So in the end, you’re the only one left. Murong Su, Murong Baek’s son. A traitor’s blood.”

“That’s right. So, the others—”

“Execute them on the spot.”

At Jeong Hogun’s firm interruption, all color drained from Murong Su’s face.

“What do you mean—”

“The Murong Family Head, Murong Baek, and his family colluded with foreign enemies, disrupted the order of the Great Nation, and caused immense harm throughout the northern frontier. This was clearly an act of treason. Not the slightest mercy can be shown in punishing it.”

“Thousand Captain!”

Blood mingled with the cry he forced out.

Crack. Murong Su snapped the arrows lodged throughout his body. His face was painted with an anguish beyond words.

“Didn’t I tell you? They—they…”

He coughed, spitting blood.

Murong Su fell to his knees, unable to finish speaking. At that moment, the family members who had watched every second of the scene from a distance could no longer bear it. They rushed through the iron gate.

“Young Master!”

“No! The Young Master is innocent!”

As they ran toward him, crying out in desperation, Jeong Hogun slowly raised a hand.

In Murong Su’s wide-open eyes, he could see hundreds of archers drawing their bows taut.

There was no choice left.

One small gesture. Or one short command.

And it would all be over. Everything.

“N-no! Please, stop!”

Murong Su’s desperate plea broke through with a spray of dark red blood.

And then, a hoarse old voice spoke from behind Jeong Hogun.

“People only show their true hearts when their lives are in danger. Don’t you agree, Thousand Captain of the Embroidered Uniform Guard?”

It was a small, elderly man.

His skin was dark, and his striking features made it clear he was not Han.

But what made the old man look especially unusual was that he wasn’t riding a horse or a mule. He was riding a person.

A huge man, one who could be compared to a bear.

“Taishan can’t understand what you’re saying. Has Namho gone senile?”

“Damn it, you’re at it again.”

The old man, Namho, didn’t flinch.

As if he had been waiting for the moment, he pulled out a chunk of jerky and stuffed it into Taishan’s mouth. Then he nodded toward Jeong Hogun.

“Anyway. In this old man’s opinion, this is probably enough for now. What do you think?”

After a moment’s thought, Jeong Hogun lowered his hand.

As his fingers slowly relaxed, hundreds of taut bowstrings lowered in silence.

“First, we’ll escort them to the government office. We’ll decide how to deal with the survivors after a thorough interrogation.”

“Do that. An old man like me doesn’t have the power to stop you from going that far. Even that much is more than they could have hoped for.”

Namho shrugged, then patted Taishan on the crown of his head.

The enormous man lowered himself, bringing Namho roughly eye to eye with Murong Su, who could only blink, still unable to make sense of what was happening.

“Did you say your name was Murong Su?”

“Y-yes. But who exactly are you, Old Man?”

“You don’t need to know the name of an old man like me. Just know that I belong to the Murim Alliance.”

“The Murim Alliance…!”

“Oh, one more thing. I’m also the Blazing Flame Divine Dragon’s—no, the Marquis of Shangshan’s representative.”

Namho smiled bitterly at Murong Su’s face, which had gone stiff as stone.

“Don’t look so surprised. I’m only offering you a chance.”

“A chance…?”

“Yes. A chance for those who haven’t strayed from the orthodox path.”

Namho knew.

No—Jin Taekyung knew.

Even in deep darkness, there was light. And even in a brilliant beam of light, there was darkness.

That was exactly why Jin Taekyung had sent Namho here.

Eliminating a future threat didn’t always mean eliminating the people themselves.

If what remained was not diseased grass and trees, but strong, green shoots, there was no reason to rip them out by the roots.

*“If we’re the orthodox faction, shouldn’t we at least live up to the name?”*

Remembering what Jin Taekyung had said before leaving the Jin Family of Taiyuan, Namho smiled faintly.

Then he spoke to Murong Su—and to all of them, the entire group who had run breathlessly to his side despite being reduced to barely a hundred people.

“From this moment on, the Murong Family no longer exists.”

“…”

“Those who abandoned benevolence and righteousness and strayed from the orthodox path can no longer belong to the Murim Alliance’s orthodox factions, nor can they be a great family.”

His voice was so powerful that it was hard to believe it came from such a small man. Though he hadn’t infused it with a single scrap of internal energy, every word rang clearly in their ears.

“But if anyone still walks the right path, the Murim Alliance will not cast them aside. That is the right thing to do.”

Namho fixed his eyes on Murong Su and continued.

“As I said, the Murong Family no longer exists. But the Murong household is another matter.”

This wasn’t a decision he had made on his own.

Every sect in the north had agreed to it. The Murim Alliance had decided.

“If your innocence is proven in the future, the Murong family will have another chance to prove itself under a new Family Head.”

“…”

“…”

At that moment, the hundred or so members of the family trembled.

A final chance had been given to people who had thought everything was over.

They had been given the chance to prove their innocence—to prove themselves.

All thanks to the sacrifice and courage of the one man who hadn’t abandoned them to the very end.

“Young Master!”

No longer retainers of the Murong Family but of the Murong household, they surrounded Murong Su with fervent voices and shining eyes.

The man they would soon call their Family Head.

As Namho watched the scene with a calm gaze, he suddenly remembered something he had forgotten and smiled faintly.

The Five Great Families.

Together with the Nine Sects and One Gang, they were the fifteen pillars holding up the vast world of the Nine Provinces.

He already knew who would fill the fifth empty seat, left behind by the Murong name.

No—in fact, all the martial world knew.
```
