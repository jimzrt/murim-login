<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0930.txt",
      "sha256": "7299314eed40469c5429e176b2c0c9e5fc155d5447142cc4d1fc09449fdae900",
      "bytes": 13483
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "db3f0bad6a545e7328b8f442eceb86a9d4ac681f15460b81890597089e7b4824",
      "bytes": 2431
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0666305ef3a14502bbfe5c72134a55888b76af6f3fad7264eaf0463c809292b0",
      "bytes": 231946
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f3da6515306c24b733ef53431357dfbd321a9538f7864cbcc7eab30541b10ef8",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "5cc625a9e3685217d52664db367ad4509508884e149745e9f3fe3ad28fe71d29",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4a4a60888ef3da7b9051cd9e212773170ac4298933282cce3997375f98d76ac9",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8463e0cd973eea07575df55451f7ec50e3f216833117ffa2f2585cf36eb2f997",
      "bytes": 1343
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7ead5c16f5ed99bb824ca68601f1f331f244bb24206167da8456b101624e7941",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "f7209486322537049f1446c85bda45249e1b596fec516205ecf5514380f9f95e",
      "bytes": 973
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "96eb8ce78e33a57a9ddbe5492d597b5dae1f0866631c0897c81ff6f63a94a517",
      "bytes": 839
    },
    {
      "path": "characters/Namho.md",
      "sha256": "c58275018ecaf7e5da583b4e3231e878ef97ef722994f2462e1835b8c34e166a",
      "bytes": 973
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "8a583d6f2a804b6b5a1f8788404a9fc3c7892de7f5180fc742cd75829abdd2a2",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "a595864ed7bf6b2823594753436ad62f27bac7fd7c1858883ff2bab730722220",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "8ea3002dc603674269c56cec4a3fbff364a9cca9250d5eff6c4ff1bf76a102df",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "889965200ee03ae2bd1c9e74b45c98310d04786950fc980aa916b222495ca2f2",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 15243
}
-->

# Durable State Update — Chapter 930

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
1 and safe_through 930. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 930. Profile updates may replace only one
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
  "chapter": 930,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 930,
    "continuity_sources": [930],
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
    "Zhu Bao is Crown Prince; the Emperor is his older brother and supports his compassionate vision of rulership.",
    "The Emperor ordered a purge of treason suspects, promising to spare the innocent after their connections are established.",
    "Jeong Hogun’s marketplace appeal and song were made under the Emperor’s command; the former Grand Preceptor and thousands of supporters of Zhu Bao joined Hogun’s Embroidered Uniform Guard against the traitors.",
    "The fighting in the imperial capital ended with the rebel forces routed and scattered; an unidentified person woke three days later.",
    "The Martial God’s letter to the Bow Saint described a chosen one who would bring a new dawn; Taekyung concluded that the Martial God was also a System user, a Player.",
    "The Bow Saint believes Taekyung is the chosen one, tested him, and relayed the Martial God’s message; she used the Imperial Palace’s information network while disguised as an attendant.",
    "The Emperor knows nothing of the Bow Saint’s mission beyond a vague suspicion.",
    "Aehyang, the City Lord of Sichuan Province’s favorite concubine, was a Dark Heaven agent who infected him with the Blood Soul Gu while he was in the Imperial Capital.",
    "The Bow Saint sent the gravely ill City Lord back to Sichuan so someone around Taekyung might discover the cause.",
    "The Bow Saint says Dark Heaven has infiltrated Great Nation local officials and military leadership, potentially including provincial City Lords.",
    "Taekyung collapsed after hearing the Martial God’s message; Jeok Cheongang took him away to rest."
  ],
  "continuity_sources": [
    928,
    929
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "What story has So Gyo kept to herself?",
    "Where is Ma Sanbao, and what is his current status?",
    "Who woke three days after the fighting ended, and what is their condition?"
  ],
  "safe_through": 929,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기.",
    "Render 황태제 as “Crown Prince” in this succession context.",
    "Render 반정 as “restoration” for the political movement in this chapter."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 사천당가   | **Sichuan Tang Clan**            |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 팀장      | **Team Leader**       |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 대한민국 | **Korea** | Country reference. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 은자 | **silver nyang** | Silver currency unit. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 야명주 | **night-shining pearls** | Pearls embedded in the cavern ceiling that provide light. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 황하 | **Yellow River** | River along which civilization began. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |
| 무영 | **No Shadow** | The concealed Supreme Peak assassin serving the Emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 주표 | 혁무진 | prince_to_subordinate_of_his_companion | Tenfold Man Hyuk Mujin | formal and playful | Zhu Bao takes Mujin’s boast literally and grants him the title. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 무영 | employer addressing a hidden assassin in his service | No Shadow | authoritative | The Emperor calls him by name and tells him to withdraw. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 황제 | 주표 | older brother addressing his younger brother and newly appointed Crown Prince | Bao’er | intimate and authoritative | The Emperor uses a warm childhood-style name before commanding Zhu Bao to accept the succession. |
| 주표 | 황제 | younger brother and Crown Prince addressing the Emperor | Your Majesty | formal and deferential | Zhu Bao formally accepts the Emperor’s command. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 928
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 922
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 928
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 928
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 928
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 922
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 928
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one who would bring a new dawn, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 912
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 922
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 922
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 922
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 922
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃930화



희한한 일이다.

분명 여느 때처럼 나를 기다리고 있어야 할 낯선 천장이 이상하게도 익숙하게 느껴지는 것은.

‘뭐지?’

서서히 또렷해지는 시야 속, 나는 천천히 눈을 돌려 주위를 둘러보았다.

단순히 침실이라고 부르기에는 턱없이 넓은 공간.

사방을 둘러싼 천들 사이사이로 굵은 기둥이 보였고, 곳곳에 배치된 화로와 천장을 별처럼 수놓은 야명주(夜明珠)로부터 흘러나온 빛이 사방을 은은하게 감싸고 있었다.

‘잠깐. 야명주?’

다음 순간, 나는 뒤늦게 이 기시감의 정체를 알아차렸다.

왠지 모를 익숙함이 느껴졌던 이유도 함께.

‘이곳은…….’

맞다.

이곳은 생활과 정무(政務)를 동시에 겸하기 위해 만들어진 거대한 전각이며, 철통같은 호위 병력으로 가득한 요새.

바로 건청궁(乾淸宮)이었다.

‘어쩐지 익숙하더라니.’

사실 야명주가 아니었더라면 상황 파악이 좀 늦었을지도 모르겠다.

청경채 마켓에 가져다 팔아도 은자 수백 냥은 너끈히 나갈 법한 씨알 굵은 야명주를 반짝이 스티커처럼 덕지덕지 처바르는 건 황제나 할 수 있는 일이니까.

‘그런데…… 내가 왜 여기에 있는 거지?’

텅 비어 버린 듯한 머릿속에서 의문이 떠오른 그 순간.

솨아.

어디선가 불어온 미세한 바람에, 침실을 둘러싸고 있던 천들이 흔들렸다.

동시에 마치 유령처럼 불현듯 나타난 흑의인이 작게 고개를 숙였다.

“기침하셨습니까.”

웅얼거리는 듯한 목소리.

때아닌 불청객을 멍하니 바라보던 나는 침착하게 상황을 파악했다.

황제의 처소. 황제의 이불. 황제의 침대. 황제의 베개.

입고 있는 옷은 온통 황금빛이고, 슬쩍 바지를 들춰 보니 속옷까지 번쩍이는 금빛 비단이다.

그야말로 킹갓엠페러 풀 세트.

거기에 더해 살수이자 초절정 고수인 황제의 암중 호위, 무영(無影)의 공손한 언행까지.

‘그렇다면 이건 설마.’

냉철한 사고방식을 통해 하나의 결론을 내린 나는 몸을 부르르 떨었다.

“빙의……!”

틀림없다. 그것 말고는 설명이 안 된다.

한숨 푹 자고 일어났더니 인생의 장르가 퓨전 무협에서 빙의물로 뒤바뀐 건에 대하여 경악을 금치 못하던 그때, 무영이 특유의 웅얼거리는 목소리로 입을 열었다.

“괜찮으십니까.”

너 같으면 괜찮겠냐는 말이 목구멍까지 솟구쳤지만, 지금은 보다 자세한 상황 파악이 우선이다.

“지금이 몇 시냐. 아니, 대연회 이후로 며칠이나 흘렀지?”

“……?”

자다 일어난 황제가 던지기에는 확실히 이상한 질문이었는지, 멀뚱멀뚱하게 나를 바라보던 무영이 대답했다.

“사흘입니다.”

“사흘?”

“예.”

“……그럼 내가 얼마나 잔 거지?”

“그 역시 사흘입니다.”

나는 눈을 질끈 감았다.

사흘. 고작 사흘 만에 모든 것이 끝장났다.

황제고 나발이고, 앞날이 창창한 이십 대 초반 훈남에서 극강 노안의 중년 아재가 되어 버린 데다가 지금까지 이루어 놓은 것들이 물거품이 되어 버렸다.

‘시스템 창…… 오픈.’

설마 하는 생각으로 내심 뇌까린 명령어는 공허하게 흩어졌다.

응당 울려 퍼져야 할 맑은 종소리도, 반투명한 홀로그램 창도 없이.

‘도대체, 도대체 어떻게 흘러가는 거지?’

숨이 막혔다.

피똥 싸며 올린 레벨도, 스탯도, 심지어는 시스템 창조차 쓰지 못해서 두 번 다시 현실로 돌아가지 못할 수도 있다.

‘잠깐만. 그렇다면 원래의 나는?’

문득 떠오른 생각에 눈이 번쩍 뜨인다. 나는 다급한 목소리로 무영을 향해 외쳤다.

“그럼 나는……. 아니, 진태경은 어찌 되었느냐!”

새카만 복면 위로 무영의 두 눈동자가 깜빡였다.

“태원진가의 진태경 말씀이십니까.”

“그래, 열화신룡 진태경 말이다! 잘생기고, 키 크고, 완벽한 근육에, 왜 여자들에게 인기가 없는지 모를 그놈!”

그리고 다음 순간 들려온 무영의 대답은, 내 사고를 정지시키기에 충분했다.

“아직 깨어나지 못한 상태입니다.”

“뭐?”

“그자는 원인 불명의 이유로 의식을 회복하지 못하고 있습니다. 말씀드리기 송구하오나, 신의(神醫)라 불리는 이가 진찰한 결과에 따르면 사실상 죽은 것이나 다름없는 상태라고 합니다.”

“……!”

“그로 인해 황태제(皇太弟) 전하께서도 벌써 사흘째 식음을 전폐하고 계십니다. 우애를 나눈 벗으로서 반드시 돌려주어야 할 것이 있다며…….”

말꼬리를 흐린 무영이 조심스럽게 내민 무언가를, 나는 멍하니 받아들었다.

거칠면서도 차가운 금속의 촉감.

마치 흑요석(黑曜石)처럼 반짝이는 그것은, 내가 최악의 상황을 대비하여 주표에게 건네주었던 사천당가의 신물이었다.

‘만독지환(萬毒指環).’

반드시 살아남아, 머지않은 미래에 다시 돌려주겠노라고 약속했던 소년의 모습이 눈앞에 어른거린다.

하지만…….

‘빌어먹을.’

어떻게 되어 버린 것인지는 모르겠지만, 개 같은 운명은 내 인생을 다시 한번 이렇게 꼬아 버렸다.

태원진가의 진태경은 이제 없다.

그리고 어쩌면 대한민국의 헌터 진태경의 삶도 이것으로 끝났다.

까드득.

어느샌가 힘껏 말아쥔 주먹이 새하얗게 물들었다. 그러나 손등에 가득한 주름을 본 순간, 나도 모르게 힘이 풀렸다.

스륵.

힘없이 풀어지는 손아귀.

동시에 거친 살갗을 타고 굴러떨어진 만독지환이 침소의 바닥에 깔린 청석(靑石)과 부딪혔다.

캉. 카강.

드넓은 공간 속에서 홀로 울려 퍼지는 서늘한 마찰음.

나는 희망이 빠져나간 눈동자로 빠르게 회전하는 만독지환을 바라보았다.

야명주의 빛과 만난 검은색 보석이 번뜩일 때마다, 이제는 두 번 다시 볼 수 없을 얼굴들이 눈앞을 스쳤다.

목숨보다 소중한 가족들을 시작으로, 최 팀장을 비롯한 수많은 동료들.

내가 믿고, 나를 믿어 주는 그들 모두의 모습이 떠올랐다.

그리고 이제야 비로소 알게 된, 나와 같은 운명을 타고난 어느 존재도 함께.

‘무신(武神).’

플레이어(Player)라는 이름의, 또 다른 시스템 사용자.

나보다 한참 앞서 이 얄궂은 운명의 선택을 받았던 사람.

그는 지금 어디에 있을까.

그 또한 나와 같은 상황을 겪었을까?

아니면 정말로 죽었기에 시스템이 새로운 플레이어로 나를 택한 것일까?

알 수 없다.

지금 당장은, 그리고 어쩌면 앞으로도 영원히.

현재의 나는 더 이상 선택받은 자도, 플레이어도 아니다.

그렇기에 모든 진실을 알고 있을 시스템은 이 의문에 대한 답을 들려주지 않을 것이다.

아니, 내가 듣지 못할 것이다.

시스템은 그런 힘이니까.

오직 한 사람을 위한 힘이니까.

‘그렇게…… 또 다른 플레이어가 나타나겠지.’

소리가 되어 흘러나오지 못한 채 그저 혀끝에서만 맴도는 공허한 뇌까림.

나는 깊게 가라앉은 눈빛으로 계속해서 회전하고 있는 만독지환을 바라보았다.

지금까지도 푸른 청석 위에서 빙글빙글, 끊임없이 돌고 있는 그것을.

“……?”

아니, 잠깐만.

뭔가 이상한데 이거.

“그, 저건 도대체 언제까지 도나?”

내 조심스러운 물음에, 무영이 대답했다.

“이래서 눈치 빠른 놈은 싫다니까.”

뭐?



* * *



조용히. 아주 조용히, 가자미처럼 가늘게 눈을 떴다.

낯선 천장이 보인다. 조금 전과는 달리 적당히 호화롭고, 적당히 무협스러운.

‘좋아. 1차 통과.’

소리도 나지 않을 만큼 미세하게 손을 들어 올렸다.

번쩍거리는 황금빛 옷자락을 보자 마음이 무거워졌다.

‘2차는 보류.’

어느새 이마에 송골송골 맺혀 있는 식은땀을 애써 무시하며, 바지를 슬쩍 들췄다.

어떤 쳐죽일 놈이 이런 걸 팬티랍시고 입혀 놨는지는 모르겠지만, 역시나 휘황찬란한 황금빛의 속옷이 보인다.

‘3차, 슬슬 개 같음.’

현실을 확인하는 것이 두려워 살짝 떴던 실눈을 다시 감았다.

불길한 징조.

하지만 아직 끝난 것이 아니다.

소름 끼치는 정적 속, 나는 바지 안으로 조용히 손을 뻗어 속옷 위를 더듬었다.

매우 익숙하면서도 눈물이 날 정도로 반가운, 동시에 이 세상에 둘도 없을 묵직한 촉감을 느끼고 몸을 부르르 떨었다.

“아, 아아.”

도무지 뭐라 형용할 수 없을 짜릿한 전류가 전신으로 퍼진다.

살았다.

난 살아 있다.

이건 조금 전처럼 그 개 같은 꿈속이 아니다. 생생한 현실이고, 살아 숨 쉬는 현재였다.

지금의 나는 헌터 진태경이자, 열화신룡 진태경이었다.

‘젠장. 이게 뭐라고.’

내가 나로 살아 있다는 것은 얼마나 감격스러운 일인가.

나는 소매를 들어 찔끔 흐르는 눈물을 닦았다.

그리고 어느 때보다 감사한 마음으로 세상을 마주하기 위해 눈을 뜬 순간.

“아.”

숨소리조차 내지 않은 채 나를 바라보고 있던 낯익은 얼굴들과 눈이 마주쳤다.

“…….”

“…….”

“…….”

“…….”

영원히 이어질 것만 같은 숨 막히는 침묵 속, 신의(神醫)가 먼저 무거운 목소리로 입을 열었다.

“충분히 그럴 수 있습니다.”

신의 옆에 서 있던 적천강이 내 시선을 피하며 말을 받았다.

“그래, 열양지기의 영향이다. 사람은 죄가 없지.”

궁성이 고개를 끄덕이며 중얼거렸다.

“과연 선택받은 자…….”

나는 조용히 심호흡했다.

마치 세상이 멈춘 듯했다.

아니, 정확히는 차라리 멈춰 버렸으면 했다.

하지만 간절한 염원을 담아 지그시 눈을 감고 다시 떴음에도, 참혹한 현실은 여전히 그곳에서 나를 기다리고 있었다.

신의. 적천강. 궁성.

그래, 여기까진 이해할 수 있었다.

산전수전 다 겪고 온갖 세상 못 볼 꼴은 죄다 지켜본, 나이 지긋한 사람들이 아닌가.

하지만 방 안에 모여 있는 사람들은 그들뿐만이 아니었다.

화룡각.

시발 화룡각.

내가 그들을. 그들이 나를.

정확히는 바지 앞섶에 손을 넣고 있는 내 모습을 보고 있었다.

믿을 수 없다는 듯이 눈을 부릅뜬 채, 뚫어지도록.

‘아.’

나는 터져 나오려는 탄식을 가까스로 삼켰다.

그러고는 최대한 담담한 어조로 입을 열었다.

“압니다. 충분히 오해할만한 모습인 거.”

“딱히 오해는 아닌 것 같, 음.”

작게 중얼거린 송일섬이 내 눈빛을 보고 입을 다물었다.

옆에 있던 사마표는 상당히 놀란 표정으로 조용히 엄지를 치켜세웠다.

……개새끼.

그 와중에 약간의 기쁨과 극도의 치욕스러움을 동시에 느끼며, 나는 재차 입술을 뗐다.

“하지만, 나름대로의 사정이 있었습니다.”

“태산이 안다! 사정 안다! 그거 뭔지 안다!”

“아가리 닥쳐 이 새끼야!”

“아.”

내 벼락같은 호통에 신나서 들썩거리던 태산이 움츠러든 그때, 어째서인지 여전히 녀석의 어깨에 목말을 타고 있던 남호가 진지한 얼굴로 입을 열었다.

“그런데, 그 손은 도대체 언제쯤 뺄 셈이냐?”

정곡을 찌르는 한 마디.

나는 당황하지 않고 침착하게 답변했다.

“그렇지 않아도 적절한 시기를 엿보던 중이었습니다.”

“음. 아무래도 이런 상황에서는 쉽게 빼기는 힘들지.”

“이해해 주시니 감사합니다.”

“그래도 보는 눈이 적지 않으니 지금이라도 빼는 게 좋다. 천천히는 말고 빠르게.”

“혹시 이유가 있을까요?”

“동작이 느리면 그만큼 시선이 쏠린다. 자, 노부가 지금부터 셋을 셀 테니, 정확히 셋에 빼거라.”

“좋은 생각이긴 한데, 그 말을 함으로써 시선이 더 쏠린 것 같은데요.”

주위를 둘러본 남호가 제법이라는 표정으로 고개를 끄덕였다.

“그것도 그렇군.”

“그냥 아무 말도 하지 말아 주십시오. 잠시만, 아주 잠시만이라도.”

“알겠다.”

조용히 입을 다문 남호를 뒤로 한 채, 나는 작게 심호흡했다.

그리고 혁무진의 옆에서 다른 곳을 쳐다보고 있는 한 사람을 향해 조심스럽게 입을 열었다.

“주 소저.”

그리고 다음 순간.

쐐애액, 쾅!

지금껏 본 적 없는 속도로 방을 뛰쳐나가는 주화란의 뒷모습과 함께, 혁무진이 다가와 내 어깨를 두드렸다.

“저는 조장님 마음 다 압니다.”

“……여물어.”

“예.”

차라리 꿈이었으면 좋겠다.
```

## Final English reading copy

```markdown
# Chapter 930

Strange.

The unfamiliar ceiling that should have been waiting for me, just like always, somehow felt familiar.

*What is this?*

As my vision slowly sharpened, I turned my eyes and looked around.

The space was far too large to call a mere bedroom.

Thick pillars stood between the curtains surrounding the room, and light spilled from braziers placed here and there and night-shining pearls embedded in the ceiling like stars, softly bathing the entire room.

*Wait. Night-shining pearls?*

The next moment, I finally realized what had been causing this sense of déjà vu.

And why the place felt so familiar.

*This is…*

That’s right.

This was a vast pavilion built to serve as both living quarters and a place to handle state affairs—and a fortress filled with an ironclad guard.

It was Qianqing Palace.

*No wonder it felt familiar.*

Actually, if not for the night-shining pearls, it might have taken me longer to figure out what was going on.

Only an emperor could plaster the place with night-shining pearls big enough to fetch hundreds of silver nyang each on Bok Choy Market, as if they were glitter stickers.

*But…why am I here?*

The question rose in my mind, which felt as if it had been emptied out.

*Whoosh.*

At that moment, a faint breeze blew in from somewhere, stirring the curtains around the bedroom.

At the same time, a man in black appeared out of nowhere like a ghost and bowed his head slightly.

“Have you awakened?”

His voice was muffled, almost a mumble.

I stared blankly at the unexpected intruder, then calmly assessed the situation.

The Emperor’s quarters. The Emperor’s blanket. The Emperor’s bed. The Emperor’s pillow.

The clothes I was wearing were all golden, and when I lifted the edge of my pants to sneak a peek, even my underwear was gleaming golden silk.

The full King-God-Emperor package.

And on top of that, No Shadow—the Emperor’s hidden guard, an assassin and Supreme Peak master—was speaking to me with such courtesy.

*Then could this be…*

I drew a conclusion through clear-headed reasoning, then shuddered.

“Possession…!”

It had to be. There was no other explanation.

I’d gotten a good night’s sleep, woken up, and my life had changed genres from fusion Murim to a possession story. Just as I was reeling from the shock, No Shadow spoke in his usual muffled voice.

“Are you all right?”

*Would you be all right?* rose to the tip of my tongue, but figuring out exactly what was going on came first.

“What time is it? No, how many days have passed since the grand banquet?”

“……?”

Apparently, it was a strange question for an emperor who’d just woken up. No Shadow stared at me blankly before answering.

“Three days.”

“Three days?”

“Yes.”

“……Then how long was I asleep?”

“Three days as well.”

I squeezed my eyes shut.

Three days. In just three days, everything had gone to shit.

Forget being an emperor—I’d gone from a handsome young man in his early twenties with a bright future to a middle-aged man with the face of an old-timer, and everything I’d achieved had gone up in smoke.

*System window…open.*

I silently tried the command, just in case.

But it scattered into the void.

There was no clear chime, no translucent holographic window.

*What the hell is going on? How did things get like this?*

I couldn’t breathe.

The levels I’d busted my ass to gain, my stats—and now I couldn’t even access the System window. I might never return to the real world.

*Wait. Then what happened to the original me?*

The thought suddenly struck me, and my eyes flew open. I shouted at No Shadow in a panicked voice.

“Then what happened to me…? No, what happened to Jin Taekyung!”

Above his pitch-black mask, No Shadow blinked.

“You mean Jin Taekyung of the Jin Family of Taiyuan?”

“Yes, the Blazing Flame Divine Dragon, Jin Taekyung! The guy who’s handsome, tall, and perfectly muscled, and I have no idea why women aren’t all over him!”

The answer No Shadow gave me next was enough to make my mind go blank.

“He has yet to awaken.”

“What?”

“For reasons unknown, he has not regained consciousness. I regret to report that, according to the examination of the one called the Divine Physician, he is as good as dead.”

“……!”

“As a result, His Highness the Crown Prince has not eaten or drunk anything for three days. He said there was something he must return to a friend with whom he shared a bond…”

No Shadow trailed off, then carefully held something out to me. I accepted it in a daze.

The feel of rough, cold metal.

It gleamed like obsidian. It was the divine artifact of the Sichuan Tang Clan—the one I’d given Zhu Bao in case the worst happened.

*The Myriad-Poison Ring.*

The boy who’d promised to survive and return it to me before long appeared before my eyes.

But…

*Damn it.*

I didn’t know how things had turned out this way, but that shitty fate had twisted my life into knots once again.

Jin Taekyung of the Jin Family of Taiyuan was gone.

And perhaps the life of Jin Taekyung, the Hunter from Korea, had ended here too.

*Crack.*

At some point, my fist had clenched so hard my knuckles had gone white. But when I saw the wrinkles covering the back of my hand, the strength left me.

*Slide.*

My fingers loosened helplessly.

At the same time, the Myriad-Poison Ring rolled over my rough skin and fell, striking the bluestone floor of the bedroom.

*Clang. Clang.*

A cold metallic sound rang through the vast space, all alone.

With hope drained from my eyes, I watched the Myriad-Poison Ring spin rapidly.

Each time the black gem caught the light of the night-shining pearls and flashed, faces I would never see again crossed my mind.

My family, more precious to me than my own life, and all the countless comrades who stood with me, starting with Team Leader Choi.

They all came to mind—every one of them, the people I trusted and who trusted me.

And now, at last, I understood there was another being born to the same fate as me.

*The Martial God.*

Another System user, known as a Player.

Someone who had been chosen by this cruel fate long before I was.

Where was he now?

Had he gone through the same thing I had?

Or had the System chosen me as a new Player because he really was dead?

I didn’t know.

Not right now, and perhaps never.

I was no longer the chosen one. I was no longer a Player.

And so the System, which knew the whole truth, wouldn’t answer these questions.

No—it was me who wouldn’t hear the answers.

That was the power of the System.

A power meant for one person alone.

*So…another Player will appear.*

The empty thought never made it past the tip of my tongue.

With my eyes sunk deep, I kept watching the Myriad-Poison Ring spinning.

It was still turning and turning on the blue bluestone floor, without end.

“……?”

Wait a second.

Something about this is weird.

“H-how long is that thing going to keep spinning?”

At my cautious question, No Shadow answered.

“That’s why I hate people who catch on too fast.”

What?

* * *

Quietly. Very quietly, I opened my eyes to slits, like a flounder.

An unfamiliar ceiling came into view. Unlike the one from a moment ago, this one was moderately luxurious and moderately Murim-like.

*Good. First check passed.*

I raised a hand so slightly it made no sound.

Seeing the glittering golden sleeve weighed on my heart.

*Second check, pending.*

Ignoring the cold sweat beading on my forehead, I carefully lifted my pants.

I had no idea which son of a bitch had put this on me and called it underwear, but sure enough, it was dazzlingly golden.

*Third check. This is getting shitty.*

Afraid to confirm reality, I closed my barely open eyes again.

A bad sign.

But it wasn’t over yet.

In the awful silence, I quietly reached inside my pants and felt over my underwear.

The familiar, tearfully welcome, and utterly unique weight of it made my whole body shudder.

“Ah, ah…”

An indescribably thrilling jolt spread through my entire body.

I was alive.

I was still alive.

This wasn’t that shitty dream from a moment ago. This was vivid reality, the present in which I was alive and breathing.

I was Jin Taekyung the Hunter and Jin Taekyung the Blazing Flame Divine Dragon.

*Damn it. What a thing to be grateful for.*

How moving it was to be alive as myself.

I wiped away a few tears with my sleeve.

And just as I opened my eyes to face the world with more gratitude than ever—

“Ah.”

My gaze met a group of familiar faces who’d been watching me without making so much as a sound.

“……”

“……”

“……”

“……”

In the suffocating silence that felt like it would last forever, the Divine Physician spoke first, his voice grave.

“That is perfectly understandable.”

Jeok Cheongang, standing beside the Divine Physician, avoided my gaze as he chimed in.

“Yes, it’s the Scorching Yang Qi. He’s done nothing wrong.”

The Bow Saint nodded and murmured,

“Truly the chosen one…”

I took a quiet, deep breath.

It was as if the world had stopped.

No—more accurately, I wished it would stop.

But even after I shut my eyes tight, made a fervent wish, and opened them again, the dreadful reality was still waiting for me right there.

The Divine Physician. Jeok Cheongang. The Bow Saint.

Yes, I could understand them.

They were all old enough to have been through thick and thin, to have witnessed every sight the world could offer.

But they weren’t the only ones gathered in the room.

The Fire Dragon Pavilion.

Fuck. The Fire Dragon Pavilion.

I was looking at them. They were looking at me.

More precisely, they were staring at me with their eyes wide, as though they couldn’t believe what they were seeing—at the sight of my hand inside the front of my pants.

*Ah.*

I barely swallowed the sigh that was about to burst out.

Then, as calmly as I could, I spoke.

“I know. It looks like there’s plenty of room for misunderstanding.”

“I don’t think it’s really a misunderstanding, mm.”

Song Ilseom muttered under his breath, then shut his mouth when he saw my eyes.

Beside him, Sama Pyo raised his thumb quietly, looking rather impressed.

……You bastard.

Feeling a little pleased and utterly humiliated at the same time, I parted my lips again.

“But I had…something to take care of.”

“Taishan knows! Taishan knows about taking care of that! Taishan knows what it is!”

“Shut your mouth, you bastard!”

“Ah.”

Taishan had been bouncing with excitement, but shrank back at my thunderous shout. For some reason, Namho was still perched on his shoulders, riding him like a human throne. He spoke with a serious expression.

“But when are you planning to take that hand out?”

He’d hit the nail on the head.

I kept my cool and answered without panicking.

“I was just waiting for the right moment.”

“Mm. In a situation like this, it can’t be easy to pull it out.”

“Thank you for understanding.”

“Still, there are a lot of eyes on you. You should pull it out now. Don’t do it slowly—do it quickly.”

“May I ask why?”

“If you move slowly, people will stare longer. Here, I’ll count to three. Pull it out exactly when I get to three.”

“That sounds like a good idea, but I think saying that has drawn even more attention.”

Namho looked around, then nodded with an impressed expression.

“That’s true.”

“Please just stop talking. For a little while—even just a little while.”

“Understood.”

Leaving Namho behind as he quietly shut his mouth, I took a small breath.

Then I carefully spoke to the one person standing beside Hyuk Mujin and staring off in the other direction.

“Young Lady Ju.”

The next moment—

*Whoosh. Bam!*

As Ju Hwaran bolted out of the room at a speed I’d never seen from her before, Hyuk Mujin came over and patted my shoulder.

“I understand exactly how you feel, Captain.”

“……Shut it.”

“Yes, sir.”

I wished it had just been a dream.
```
