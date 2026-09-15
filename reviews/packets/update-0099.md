<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0099.txt",
      "sha256": "2af4660e5de68c0772ebafdf2cf5e2996666a112f6c304e39ba262962bdad3d3",
      "bytes": 15156
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f949bcdcb39842f1f64a181f0775ec7a987c58e9439b8129ecb059bbda9a25d4",
      "bytes": 3541
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8c5e8b96be5f9aca3aea3f792b4623838a9f9dfb15b8e5d04288a0abbb919749",
      "bytes": 11955
    },
    {
      "path": "characters/Im Chunsoo.md",
      "sha256": "46e142757fcd0068ec93f5ff404214abf7abc566da5f5dcd70830dff80d22b93",
      "bytes": 666
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8cf8ccd482cd7523df49fe39a76e76e414dd2eb872645047e60c42e021a0bbe7",
      "bytes": 23942
    },
    {
      "path": "characters/Kim Gwondong.md",
      "sha256": "d94a51b6c6abc172a1a51a29a962bf8eed0105024b489bbab934ce27f1630033",
      "bytes": 629
    },
    {
      "path": "characters/Kim Junsu.md",
      "sha256": "2f48547b2e8cd4d0ac14f6fd5ec83945d4d343bbda1efaa42e447b37902b6a72",
      "bytes": 594
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fb25cc71f2a3da2a6f59b9b2cba71825bb87bbb1fc11e0d23eab1eb7affac95c",
      "bytes": 11149
    }
  ],
  "estimated_tokens": 16202
}
-->

# Durable State Update — Chapter 99

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 99. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 99. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 99,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 99,
    "continuity_sources": [99],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Sangdong Guild's Security Team is monitoring Jin Taekyung with its sole Familiar mage, Kim Junsu, and multiple C-rank stealth and tracking Hunters.",
    "Kim Junsu is a C-rank mental mage who uses Familiars and is suffering from exhaustion and anxiety about his hair loss.",
    "Kim Gwondong is a Level 42 C-rank Security Team Hunter assigned to surveillance and disguises himself as a friendly neighbor.",
    "The Security Team has been watching Taekyung for days and has installed eavesdropping-magic Equipment in nearby real-estate offices.",
    "The Security Team uses a black Level 2 Cat Familiar to track Taekyung after he leaves home.",
    "Taekyung detects the black kitten as a Familiar and recognizes Kim Gwondong's disguise, while continuing to keep his own suspicions concealed.",
    "The Security Team Leader is offended by the real-estate ajumma's old-bachelor insult, leaves for a sauna, and orders his subordinates to prepare a transcript and individual opinion statements.",
    "Taekyung learns of three properties traded within five days and five hundred meters of his home: Building 5, Unit 901; Building 4, Unit 302; and Building 3, Unit 202.",
    "Taekyung scans the apartment complex and parking lot with Qi Sense while carrying a Familiar and finds no suspicious vehicles.",
    "The watchers are using one of the three recently traded apartments as a surveillance base, but the exact property remains unknown.",
    "Hong Woojin infiltrates Taekyung's home as a kitten Familiar and is recognized by Taekyung after Hayeon keeps him confined and he soils her bedding to escape.",
    "Hayeon leaves for the library, leaving Taekyung alone with the black and white Familiars.",
    "Taekyung draws the curtains, searches his home with mana-detection Equipment, detects no mana, and makes a suspicious phone call as bait.",
    "The Security Team interprets the call as evidence of a secret plan and concludes that Taekyung possesses a USB."
  ],
  "continuity_sources": [
    98
  ],
  "open_questions": [
    "Why did Sangdong Guild's Guild Master issue a special warning about Taekyung?",
    "Who commissioned the surveillance operation and who is directing it?",
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Whether the Security Team's operation and Hong Woojin's investigation share the same commissioning chain remains unresolved.",
    "Whether the surveillance team has identified Taekyung's deliberate deception remains unresolved.",
    "Who Taekyung called remains unknown.",
    "Whether Taekyung actually possesses a USB remains unknown."
  ],
  "safe_through": 98,
  "temporary_decisions": [
    "Render 정신계 마법사 as mental mage and 보안팀 as Security Team.",
    "Use Kim Junsu, Kim Gwondong, Nabi, and Goyang for 김준수, 김권동, 나비, and 고양시.",
    "Render 개냥이 as dog-cat with an explanatory footnote.",
    "Use target, Familiar, Link, and eavesdropping-magic Equipment for 표적, 패밀리어, 링크, and 도청 마법 장비.",
    "Render 도청 마법 as wiretapping magic when referring to the magic itself.",
    "Render 월세 as monthly rent and 전세 as jeonse lease.",
    "Render 홀아비 냄새 as old-bachelor smell.",
    "Render 현자 타임 as post-nut clarity in Hong Woojin's comic internal narration."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 레벨               | **Level**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 평화 | **Peace Guild** | Guild name. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |

## Listed compact profiles

### Im Chunsoo.md

# Im Chunsoo (임춘수)

- **Safe through:** Chapter 93
- **Aliases:** Frozen
- **Role:** A-rank Hunter; founder and Guild Master of Sangdong Guild; renowned ice mage
- **Personality:** Intimidating, severe, and extremely short-tempered, though he has tried to moderate his temper with age
- **Voice:** Sharp and commanding, with a comparatively gentle tone when deliberately controlling his temper; becomes violently profane when enraged
- **Relationships:** Father of Im Changsoo, whom he considers a pathetic disappointment and immediately fires and punishes after learning of Changsoo's actions

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 98
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Kim Gwondong.md

# Kim Gwondong (김권동)

- **Safe through:** Chapter 98
- **Aliases:** None
- **Role:** Level 42 C-rank Hunter in Sangdong Guild’s Security Team, specializing in surveillance and disguise.
- **Personality:** Cautious, observant, pragmatic, and cynical about his superior’s orders and accountability.
- **Voice:** Friendly and ordinary while acting as a neighbor; deferential aloud to his Team Leader and profane internally.
- **Relationships:** Works under the unnamed Security Team Leader and cooperates with Kim Junsu and the other surveillance Hunters.

### Kim Junsu.md

# Kim Junsu (김준수)

- **Safe through:** Chapter 98
- **Aliases:** None
- **Role:** C-rank Hunter in Sangdong Guild’s Security Team; the Guild’s sole Familiar mage and a rare mental mage.
- **Personality:** Exhausted, anxious about his worsening hair loss, dutiful, and privately profane about his workload.
- **Voice:** Polite and restrained aloud; internally self-pitying, sarcastic, and profane.
- **Relationships:** Works under the unnamed Security Team Leader alongside Kim Gwondong and other surveillance Hunters.

## Korean source

```text
＃99화



보안팀장이 한 통의 전화를 받은 것은 사우나를 막 끝마친 직후였다.

- 팀장님. 접니다, 김권동.

“어, 녹취록이랑 소견서 다 썼냐?”

- 아뇨. 그게 아니라…….

“이 자식이 진짜. 최고참이라고 편의 봐줬더니 정신 못 차리지? 당장 10분 안에 소견서 작성해서 보내.”

- 아이 참, 그게 아니고요. 특이 사항 때문에 보고드리려고 전화한 겁니다.

잠시 후, 보안팀장은 들고 있던 맥반석 계란을 툭 떨궜다.

“USB를 갖고 있었다고?”

- 네. 통화 상대가 누군지는 모르지만 물건 잘 갖고 있다면서, 본인도 슬쩍 꺼내서 확인했다고 합니다. 준수가 직접 봤다니까 확실합니다.

“그, 그래서?”

- 표적이 직접 보관 중이라는데…… 당장은 준수도 어떻게 할 방법이 없어서 보고드립니다.

“준수, 준수는? 당장 바꿔 봐.”

- 지금 패밀리어로 표적 감시 중이라 곤란할 것 같은데요.

보안팀장은 입술을 질끈 깨물었다. 방금 보고받은 내용으로 머릿속은 뒤죽박죽이었다.

‘전화 상대는 누구지? 표적의 정체는? USB 안에는 대체 뭐가 들어 있을까?’

보안팀장의 본능이 꿈틀거리기 시작했다.

“김권동이. 이거 길드장님께서 특별 지시 하신 거야. 알지? 내가 몇 번이나 말했잖아.”

- 그거야 다들 알죠.

“뭐 하나라도 건지면 다 같이 대박 나는 거라고. 나도 위로 올라가고, 너도 짬 먹을 만큼 먹었으니까 팀장 달아야 할 거 아냐.”

- ……그게 제 맘처럼 되나요. 적어도 B급은 되어야 팀장 달아 주는 거 모르는 처지도 아니고.

“내 생각에 이거 충분히 건수 된다. 진태경 그놈이 어디에서 굴러먹다 온 놈인지는 모르겠는데 그림 딱 나와. 우리 상동 길드 언급하면서 대화하는 내용만 들어 봐도 알잖아. 그치?”

- 저도 좀 그렇게 생각하긴 했습니다.

계획은 차질 없이 진행되는 중이며, 상동 길드는 아직 눈치채지 못했다. 그리고 물건은 잘 간수하고 있다.

정체를 알 수 없는 상대와 진태경의 대화는 제삼자가 듣기에도 충분히 의미심장한 내용이었다.

하물며 상동 길드의 보안팀이라면 말할 것도 없다.

“그 USB가 핵심이야. 막말로 진태경이 소속된 평화 길드건, 어느 경쟁 길드건 간에 우리 길드 한번 엎으려고 수 쓰는 거면…….”

- 그런 거면 진짜 특급 정보죠.

보너스는 기본이고 승진은 옵션이다. 길드장의 눈에 든다면 무난하게 길드 임원까지 노려 볼 수 있다.

지금 이 순간, 보안팀장은 길드장의 오른팔이 된 자신의 모습을 상상했고 김권동은 상동 길드 최초의 C급 팀장이 되는 꿈에 젖었다.

“계속 주시해. 난 일단 윗선에 보고하고 진태경 통화 내역부터 조회할 테니까.”

- 넵!

“나 옷만 갈아입고 바로 간다. 아무리 늦어도 저녁 먹기 전에 표적이 어떤 놈이랑 통화했는지 뜰 테니까 그전까지 대책을 세워 보자고.”

보안팀장이 탈의실로 달려가려던 그때였다.

- 아, 팀장님. 그런데 한 가지 걱정되는 부분이…….

“뭔데.”

김권동의 목소리에서 불안함이 읽힌다. 그리고 불길한 예감은 빗나가지 않고 적중했다.

- 홍우진이 있잖습니까.

“아, 젠장.”

실수다. 너무 흥분한 나머지 홍우진의 존재를 잠시 잊고 있었다. 보안팀장은 마음이 조급해졌다.

‘그놈이 먼저 움직이면 곤란한데.’

그가 아는 길드장, 임춘수는 상벌이 명확한 인물이었다.

신입이어도 실력을 입증한다면 출셋길에 아스팔트를 깔아 주고, 아니다 싶으면 10년을 근무한 길드원이라도 망설임 없이 쳐 내는 성격.

‘한두 번 본 게 아니지.’

단순히 홍우진에게 공(公)만 뺏기고 끝날 리가 없다. 보안팀장 자신의 밥그릇이 달려 있다.

돈? 그따위 문제가 아니다. 반평생을 몸담은 길드, 올라갈 수 있는 데까지는 가 보고 싶었다.

“권동아.”

- 예.

“그놈, 지금 집에 혼자랬지?”

- 팀장님, 설마? 안 됩니다!

“아직 말 안 끝났다.”

목소리가 커진 김권동과는 달리 보안팀장은 침착했다.

“이 일, 표적 제압하고 물건 챙겨서 가면 깔끔하게 끝난다. 어차피 C급이야, 쫄 거 없어.”

- 구린내가 풀풀 나는 C급이죠. 잘못 건드렸다가 저희가 역으로 당할 수도 있습니다.

“당해? 이제 겨우 C급으로 각성한 풋내기한테 B급 베테랑인 내가? 이거 자존심 상하네.”

- …….

“너, 설마 임창수가 했던 말 믿는 건 아니지? 그게 사실이면 진태경이 사실은 A급 헌터라는 소린데…… 그럴 거면 차라리 길드장님이 첩자라고 해라. 응?”

- 아니, 무슨 말씀을 그렇게까지 하세요.

“됐고. 할 거야, 말 거야?”

- 하, 씨. 미치겠네.

깊은 한숨을 푹푹 내쉬던 김권동이 마음의 결정을 내린 것은 잠시 후였다.

- 우리 이거 걸리면 범죄자 되는 겁니다. 아시죠?

“알지. 안 걸리면 무죄라는 것도.”

- 팀장님, 진짜 간도 크시네요.

“그러니까 팀장이지. 애들은?”

- 지금 다 모여 있습니다. CCTV 파악은 투입된 첫날에 끝냈고 간단한 변장 장비도 있어요.

“좋아.”

- 언제 시작합니까?

보안팀장은 마른 입술을 핥았다.

“내가 도착하는 즉시.”

옛말에 이르기를 쇠뿔도 단김에 빼라고 했다. 그에게 있어 C급 헌터는 한 손으로도 뽑을 수 있을 만큼 물렁한 뿔이다.



* * *



낚시가 성공했다고 느낀 것은 얼마 지나지 않아서였다.

야옹.

미야옹.

내 환심을 사기 위한 두 패밀리어의 애교 세례. 그러나 이번에는 좀 다르다.

짧은 다리로 버둥버둥 소파에 올라오더니 다른 곳도 아닌 허벅지 위에 자리 잡는 모습을 보니 확신이 들었다.

‘미끼를 물었구나.’

주머니에 들어 있는 USB가 미끼다. 감시자들은 지금쯤 궁금해서 미칠 지경일 거다.

내가 통화에서 말한 계획과 전화를 받은 상대방은 누군지, 이 USB에는 도대체 뭐가 들어 있는지.

‘생각보다 과감한 놈들이었으면 좋겠는데.’

그들이나 나나, 오래 끌어서 좋을 게 없다. 평일 오후, 아파트 단지는 한적했고 TV에서는 재미없는 귀농 다큐멘터리가 방영되고 있었다.

“아, 오랜만에 뒷산이나 갈까…….”

혼잣말을 중얼거리고 현관문을 나서려던 그때, 기다리던 변화가 일어났다.



[Lv.2 고양이]

[Lv.2 고양이]



패밀리어 마법의 해제. 이 현상이 뜻하는 바는 명백했다.

‘이제야 본격적으로 움직이는구나.’

새끼 고양이의 몸으로는 내게서 USB를 훔칠 수 없다. 하지만 표적인 내가 직접 인적이 드문 곳으로 이동한다면 이야기가 달라진다.

‘누가 봐도 고만고만한 C급 헌터, 마음 놓고 뺏을 수 있다고 생각하겠지.’

물론 그 과정에 적당한 폭력과 협박도 포함되어 있을 거라는 건 충분히 예상할 수 있었다.

단, 감시자들은 가장 중요한 한 가지를 착각했다.

바로 나라는 존재다. 항상 가해자였던 그들은 자신들이 피해자가 될 수도 있을 거라는 생각을 하지 못한다.

‘기대되네. 어떤 놈들일지.’

허락 없이 불법 스토킹을 하면 어떻게 되는지 똑똑히 보여 줄 생각이다.



* * *



진태경이 부동산에서 얻은 정보는 절반만 맞았다. 상동 길드의 보안팀과는 달리 홍우진의 아지트는 그가 전혀 예상치 못한 곳에 있었다.

바로 진태경이 사는 아파트 옥상이었다.

“후우.”

패밀리어와의 링크를 해제한 홍우진은 옥상에 딸린 자그마한 비품 창고에서 눈을 떴다.

그는 경비원에게 약간의 돈을 찔러 주는 것으로 5평 남짓한 최적의 공간을 며칠간 마련할 수 있었다.

“이거 일이 더럽게 꼬였네.”

심상치 않은 진태경의 통화, 뭐가 담겼는지 모를 USB.

드디어 정보라고 할 만한 걸 알아냈지만 그건 상동 길드 쪽도 마찬가지다.

비품 창고에서 나온 그는 옥상 밑을 내려다봤다. 까마득한 저 아래, 막 아파트 입구를 나서는 진태경이 보였다.

‘따라가야 하나, 말아야 하나.’

의뢰를 생각한다면 따라가는 게 맞는데, 어쩐지 꺼림칙하다. 홍우진이 갈등하는 눈빛으로 멀어져 가는 진태경을 지켜보던 그때였다.

“허, 이것 보게?”

한 명, 그리고 다시 한 명. 슬금슬금 기어 나오는 꼴이 딱 먹이를 노리는 뱀의 그것과 다르지 않다.

그 숫자가 도합 여섯.

각자 복장도 다르고 행동거지도 일반인과 다름없지만 업계 동업자인 홍우진의 눈에는 똑똑히 보였다.

“상동 길드 놈들이군.”

한두 명도 아니고 자그마치 여섯이 몰려나왔다.

더군다나 표적의 목적지는 인적이 드문 야산. 곧 벌어질 일을 짐작한 그가 미간을 찡그렸다.

“가지가지 한다. 아주.”

무력행사는 홍우진의 기준에서 벗어나는 일이다. 처음 의뢰를 맡을 당시 신신당부를 했음에도 보안팀을 투입시켰을 때 관뒀어야 했는데……. 이건 도를 지나쳤다.

‘진태경, 저놈은 내 손으로 털고 싶었는데.’

정체가 궁금해지는 놈이지만 딱 여기까지다. 더 이상 얽히면 안 될 것 같다는 예감이 들었다.

‘상동 길드, 이 양아치 새끼들.’

혀를 찬 홍우진이 스마트폰을 꺼내 문자를 발송했다.

수신인은 1팀장. 문자 내용은 짧고 간략했다.



〈 1팀장



일 접습니다.



옥상을 떠나기 전, 이미 사라진 진태경의 명복을 빌어 주는 것도 잊지 않았다.

‘거, 더러웠고 다신 보지 말자.’

그로서는 여러모로 재수 옴 붙은 의뢰였다.



* * *



묵묵히 산길을 올랐다. 이미 등산로를 벗어난 지 오래다.

하지만 멈추지 않는다. 깊숙이, 더 깊숙이 계속해서 걸음을 옮길 뿐.

그러던 어느 순간 너른 평지가 모습을 드러냈다. 무릎에 닿을 정도로 높이 자란 잡초가 무성한 그곳에서, 나는 천천히 돌아섰다.

“아직도 산책 중이신가 봐요?”

앞서 두 차례 마주친 바가 있는 중년인, 김권동은 말없이 얼굴을 굳혔다.

“대답이 없으시네. 옆에 계신 분은 누구?”

“친구.”

김권동이 어디서나 찾아볼 수 있는 흔한 인상이라면 지금 대답한 이 남자는 정반대였다.

조폭도 울고 갈 만큼 험악한 인상에 거구의 소유자. 그의 입술 사이로 걸걸한 음성이 흘러나왔다.

“다 알면서 왜 여기까지 왔지?”

“뒤에서 졸졸 따라오시길래. 어디까지 따라오나 본 거죠. 똥개 훈련이라고 생각하시면 편해요.”

남자가 너털웃음을 터트렸다.

“어린놈이 당돌하네. 몇 살이냐?”

“역마살이요.”

“매를 버는 재주가 있구나.”

“칭찬 감사합니다, 최병일 씨.”

남자, 최병일이 입을 다물었다. 그의 눈동자가 흔들렸다.

“……어떻게 알았지?”

“그거야 영업 비밀이죠. 그런데 김권동 씨랑 친구 맞아요? 외관상으로 봤을 때는 투샷이 영 아닌데.”

이번에는 김권동이 당황할 차례다. 하지만 내 말은 아직 끝나지 않았다.

“친구가 아니라 대답하기 곤란한가? 그럼 다른 네 분한테 물어볼게요. 박형진, 오규현, 이민철, 김준수 씨는 솔직하게 대답해 주셨으면 좋겠네요.”

우우웅.

허공이 일렁이더니 네 사람이 뚝 떨어져 내린다. 머리 위로 레벨창을 각자 달고 있는 그들은 귀신이라도 본 듯한 얼굴이었다.

“다들 뭘 그렇게 놀라시나. 숨이라도 편하게 쉬시라고 배려해 드린 건데.”

최병일이 이를 악물었다. 처음의 여유는 온데간데없고 초조함과 당황에 물든 얼굴이다.

“이런 씨팔…… 너 뭐 하는 새끼야?”

먼저 욕 박았으니까 어른 공경은 여기서 끝이다. 나는 최병일을 보며 피식 웃었다.

“아직도 몰라? 내 정보 싹 긁었을 텐데. 패밀리어까지 붙여 놓을 정도면 말 다 한 거지.”

“……!”

“집에 나 혼자였으면 그러려니 했겠는데, 가족들까지 감시당할 거 생각하니까 좀 열받더라고. 그래서 미끼 한번 던져 봤더니 덥석 물데?”

여섯 명의 감시자들이 몸을 부르르 떨었다.

“그, 그럼 USB도?”

“아, 그거? 내가 평생을 바쳐 모은 야동 컬렉션.”

인벤토리에 소중히 보관해 놨던 인류의 보물이다.

“말도 안 돼! 분명히 촉이 왔는데.”

“음. 말도 안 되는 작품들이 수두룩하긴 하지. 남자라면 촉이 오는 것도 당연한 거고.”

하나같이 망연자실한 얼굴로 서 있는 그들을 향해 말했다.

“성실하게 대답해 줬으니까 나도 하나만 물어보자.”

한 명, 한 명. 나와 눈이 마주칠 때마다 몸을 움찔거린다.

마침내 내 시선이 멈춘 곳에는 빼빼 마른 20대 남성이 서 있었다. 아마도 이놈이 패밀리어 마법사겠지.



[Lv.41 김준수]



“준수야. 너희 상동 길드에서 보내서 왔지?”

“입 닥쳐!”

최병일이 외쳤지만 김준수는 이미 대답을 끝낸 후였다.

핏기 하나 없이 창백해진 얼굴이 바로 그의 대답이다.

“오케이, 상동 길드. 그럴 줄 알았다.”

내 말을 들은 최병일의 얼굴이 딱딱하게 굳었다.

“그 이름은 입에 담지 말았어야지.”

“왜, 죽이게?”

“……널 사로잡고 생각해 보지.”

“그거 되게 힘들 텐데.”

최병일의 레벨은 60대 중반. 느껴지는 기세는 임창수와 비등하고 나머지는 그저 그런 3, 40레벨 정도의 C급이었다.

전문적인 레이드 팀도 아닌 이들이 나를 사로잡을 확률은 매우 희박하다.

“죽을 각오로 덤벼. 그래야 내 손목에 나비매듭이라도 묶을 수 있지.”

“쳐!”

최병일의 외침과 함께 상동 길드의 감시자들이 사방에서 달려들기 시작한다.

쉬이이익!

어깨 위로 떨어지는 단검 한 자루가 시작이다.

나는 느릿느릿하게만 보이는 그 궤적을 향해 손을 뻗었다.

그와 동시에…….

‘인벤토리 오픈. 장착.’

콰직!

공력을 한껏 머금은 검날이 적의 단검을 부쉈다. 이름 모를 잡초 위로 조각난 날붙이와 누군가의 핏물이 쏟아진다.

“들어와, 이 스토커 새끼들아!”

쐐애애액!
```

## Final English reading copy

```markdown
# Chapter 99

The Security Team Leader received a phone call just after finishing up at the sauna.

“Team Leader. It’s me, Kim Gwondong.”

“Oh, did you finish writing the transcript and assessment?”

“No, sir. That’s not it…”

“You little shit. I went easy on you because you’re the most senior one here, and now you’re getting careless? Write up your assessment and send it to me within ten minutes.”

“Come on, that’s not it. I’m calling to report something unusual.”

A moment later, the Security Team Leader dropped the roasted egg he was holding.

“He had a USB?”

“Yes. We don’t know who he was talking to, but he said he was keeping the item safe, and he even slipped it out to check it himself. Junsu saw it directly, so it’s certain.”

“Th-then?”

“The target is keeping it on him, apparently… Junsu has no way to do anything about it for now, so I’m reporting it.”

“Junsu? Put Junsu on right now.”

“He’s watching the target with his Familiar, so that might be difficult.”

The Security Team Leader bit down hard on his lip. His head was a complete mess after hearing the report.

*Who was the person on the phone? What was the target’s true identity? And what on earth is inside that USB?*

The Security Team Leader’s instincts began to stir.

“Gwondong. This was a special order from the Guild Master. You know that, right? I’ve told you so many times.”

“Everyone knows that.”

“If we manage to get even one thing out of this, we all hit the jackpot. I’ll move up, and you’ve been around long enough that you ought to become a Team Leader, too.”

“…It’s not as simple as wishing for it. You know perfectly well they won’t make someone a Team Leader unless they’re at least B-rank.”

“I think this is more than enough to make a real score. I don’t know where that Jin Taekyung bastard came from, but the picture is obvious. You can tell just by listening to him talk about our Sangdong Guild. Right?”

“I did think it looked that way.”

The plan was proceeding without a hitch. Sangdong Guild still hadn’t noticed anything. And he was keeping the item safe.

The conversation between Jin Taekyung and the unknown person on the other end of the line was suspicious enough to sound meaningful even to a third party.

For Sangdong Guild’s Security Team, there was no question.

“That USB is the key. To put it bluntly, whether it’s the Peace Guild Jin Taekyung belongs to or some rival Guild, if they’re making a move to bring down our Guild…”

“Then that’s seriously high-value intel.”

The bonus was a given, and promotion was an option. If he caught the Guild Master’s eye, he might even be able to aim for a position among the Guild executives.

At that very moment, the Security Team Leader imagined himself as the Guild Master’s right-hand man, while Kim Gwondong became lost in a dream of becoming Sangdong Guild’s first C-rank Team Leader.

“Keep watching him. I’ll report this up the chain and start by checking Jin Taekyung’s call records.”

“Yes, sir!”

“I’ll change clothes and head over immediately. No matter how late it is, we’ll know who the target spoke with before dinner. Let’s come up with a plan before then.”

Just as the Security Team Leader was about to hurry to the changing room, Kim Gwondong spoke again.

“Ah, Team Leader. There’s one thing I’m worried about…”

“What is it?”

Anxiety could be heard in Kim Gwondong’s voice. And his ominous premonition proved accurate.

“You know Hong Woojin, right?”

“Ah, damn it.”

It was a mistake. He had been so excited that he had briefly forgotten about Hong Woojin’s existence. The Security Team Leader grew impatient.

*It’ll be a problem if that bastard makes the first move.*

The Guild Master he knew, Im Chunsoo, was a man who made rewards and punishments absolutely clear.

If a newcomer proved their ability, he would pave the road to advancement for them. But if he decided someone was no good, he would cut them loose without hesitation—even if they had been a Guild member for ten years.

*I’ve seen it more than once or twice.*

This wouldn’t simply end with Hong Woojin taking the credit. The Security Team Leader’s own livelihood was on the line.

Money? That wasn’t the issue. He had devoted half his life to this Guild and wanted to climb as high as he possibly could.

“Gwondong.”

“Yes.”

“That bastard is alone at home right now, isn’t he?”

“Team Leader, surely not? You can’t!”

“I’m not finished talking.”

Unlike Kim Gwondong, whose voice had grown loud, the Security Team Leader remained calm.

“If we subdue the target, take the item, and leave, this ends cleanly. He’s only C-rank, after all. There’s nothing to be afraid of.”

“He’s a C-rank who reeks to high heaven. If we make the wrong move, we could be the ones getting taken down.”

“Taken down? By a rookie who only just awakened as a C-rank? Me, a B-rank veteran? That’s insulting.”

“…”

“You don’t actually believe what Im Changsoo said, do you? If that were true, it would mean Jin Taekyung was really an A-rank Hunter… If that’s the case, you might as well say the Guild Master is a spy. Huh?”

“Come on, why are you taking it that far?”

“Enough. Are you doing it or not?”

“Fuck, this is driving me crazy.”

Kim Gwondong let out several deep sighs before finally making up his mind.

“If we get caught, we become criminals. You know that, right?”

“I know. I also know that if we don’t get caught, we’re innocent.”

“Team Leader, you really have some nerve.”

“That’s why I’m the Team Leader. What about the others?”

“They’re all gathered right now. We finished checking the CCTV on the first day we were deployed, and we have some simple disguise Equipment, too.”

“Good.”

“When do we start?”

The Security Team Leader licked his dry lips.

“The moment I arrive.”

As the old saying went, you had to pull the ox’s horn while it was hot. To him, a C-rank Hunter was a soft horn he could yank out one-handed.

* * *

It didn’t take long for me to realize that the bait had worked.

*Meow.*

*Myaow.*

The two Familiars showered me with affection, trying to win my favor. But this time, something was different.

They had struggled up onto the sofa with their short legs, then settled down—not just anywhere, but on my thighs.

*They took the bait.*

The USB in my pocket was the bait. By now, the watchers must have been going crazy with curiosity.

What plan I had mentioned during the call, who I had been speaking to, and what on earth was inside the USB.

*I hope they’re more daring than I expect.*

Neither they nor I had anything to gain by dragging this out. It was a weekday afternoon, the apartment complex was quiet, and the TV was showing a boring documentary about returning to farming.

“Ah, should I go to the hill behind the apartment for the first time in a while…?”

I muttered to myself and was about to leave through the front door when the change I had been waiting for occurred.

> **System**
>
> Level 2 Cat
>
> Level 2 Cat

The Familiar magic had been dispelled. The meaning of this phenomenon was obvious.

*They’re finally making their move.*

In the body of a kitten, they couldn’t steal the USB from me. But if I, the target, moved somewhere sparsely populated on my own, that would change things.

*Anyone looking at me would see an ordinary C-rank Hunter. They’d think they could take it from me without worry.*

Of course, it wasn’t hard to predict that a suitable amount of violence and threats would be part of the process.

But the watchers had made one crucial mistake.

What they had misjudged was me. They had always been the perpetrators, and had never imagined that they could become the victims.

*I’m looking forward to this. What kind of bastards are they?*

I intended to show them exactly what happened when someone illegally stalked another person without permission.

* * *

The information Jin Taekyung had obtained from the real-estate office was only half right. Unlike Sangdong Guild’s Security Team, Hong Woojin’s hideout was in a place Taekyung had never expected.

The rooftop of the apartment building where Jin Taekyung lived.

“Whew.”

After severing his Link with the Familiar, Hong Woojin opened his eyes inside the tiny supply closet attached to the rooftop.

By slipping the security guard a little money, he had secured this optimal space of roughly five pyeong[^1] for several days.

“This job got horribly tangled up.”

Jin Taekyung’s suspicious phone call. A USB whose contents were unknown.

He had finally discovered something that could be called information, but Sangdong Guild had discovered the same thing.

Hong Woojin stepped out of the supply closet and looked down over the edge of the roof. Far below, he could see Jin Taekyung just leaving the apartment entrance.

*Should I follow him or not?*

If he thought about the job, following him was the right choice. But something about it felt wrong. Hong Woojin was watching Jin Taekyung grow smaller in the distance with a conflicted look in his eyes when—

“Huh. What do we have here?”

One person, then another. The way they slowly crawled out was no different from snakes stalking their prey.

There were six of them in total.

Their clothes were all different, and their behavior was no different from ordinary people’s. But to Hong Woojin, a fellow professional in the industry, it was obvious.

“They’re from Sangdong Guild.”

Not one or two of them—six had emerged.

What was more, the target’s destination was a deserted hillside. Realizing what was about to happen, Hong Woojin furrowed his brow.

“They really pull every dirty trick in the book.”

Using force crossed Hong Woojin’s line. He should have quit when they deployed the Security Team, despite his repeated warnings when he first accepted the job. But this had gone too far.

*I wanted to uncover Jin Taekyung’s secrets myself.*

He was a man whose identity had made Hong Woojin curious, but this was where it ended. He had a feeling that he shouldn’t get involved any further.

*Sangdong Guild, you goddamn thugs.*

Clicking his tongue, Hong Woojin took out his smartphone and sent a text.

The recipient was the Team 1 Leader. The message was short and simple.

> **Team 1 Leader**
>
> I’m dropping the job.

Before leaving the rooftop, he also remembered to wish the already-vanished Jin Taekyung a peaceful rest.

*Well, that was filthy. Let’s never see each other again.*

In every respect, it had been a cursed job.

* * *

I climbed the mountain path in silence. It had been a long time since I’d left the hiking trail behind.

But I didn’t stop. I kept walking deeper and deeper into the mountain.

At some point, a broad clearing came into view. Weeds had grown thick there, reaching up to my knees. I slowly turned around.

“Looks like you’re still out for a walk?”

Kim Gwondong, the middle-aged man I had run into twice before, said nothing. His face hardened.

“No answer? Who’s the person with you?”

“My friend.”

If Kim Gwondong had an ordinary, forgettable face, the man who answered me was the complete opposite.

He was huge, with a vicious expression fierce enough to make gangsters cry. A rough voice rumbled from between his lips.

“You already know everything, so why did you come all the way here?”

“You kept trailing me from behind, so I wanted to see how far you’d follow. Think of it as training a mutt.”

The man let out a hearty laugh.

“Young punk’s got nerve. How old are you?”

“*Yeokmasal*.”[^2]

“You’ve got a real talent for earning a beating.”

“Thanks for the compliment, Mr. Choi Byungil.”

The man, Choi Byungil, closed his mouth. His eyes shook.

“…How did you know?”

“That’s a trade secret. But are you and Mr. Kim Gwondong really friends? Judging by appearances, you two don’t exactly look like a matching pair.”

This time, it was Kim Gwondong’s turn to panic. But I wasn’t finished.

“Is it difficult to answer because you’re not friends? Then I’ll ask the other four. Mr. Park Hyungjin, Mr. Oh Gyuhyeon, Mr. Lee Mincheol, and Mr. Kim Junsu, I’d appreciate an honest answer.”

Bzzzzzz.

The air rippled, and four people dropped straight down.

Each of them had a Level window floating over their head, and their faces looked as if they had seen a ghost.

“Why is everyone so surprised? I was just being considerate so you could breathe comfortably.”

Choi Byungil gritted his teeth. All traces of his earlier composure had vanished, leaving his face colored by anxiety and bewilderment.

“What the fuck… What kind of bastard are you?”

Since he had started with profanity, my respect for my elders ended there. I let out a quiet laugh as I looked at Choi Byungil.

“You still don’t know? You must have dug up every scrap of information about me. If you went so far as to attach Familiars, that says everything.”

“…”

“I could’ve let it go if I’d been alone at home. But the thought of my family being watched pissed me off. So I threw out some bait, and you snapped it up.”

The six watchers trembled.

“Th-then what about the USB?”

“Oh, that? It’s my collection of porn I’ve spent my whole life putting together.”

It was a treasure of humanity that I had carefully stored in my Inventory.

“No way! I definitely had a feeling!”

“Well, there are plenty of works in there that defy belief. And any man would get a gut feeling about it.”

I looked at them, standing there with faces full of despair.

“You answered honestly, so let me ask you one thing, too.”

One by one, they flinched whenever their eyes met mine.

At last, my gaze stopped on a painfully thin man in his twenties. He was probably the Familiar mage.

> **System**
>
> Level 41 Kim Junsu

“Junsu. You were sent here by Sangdong Guild, weren’t you?”

“Shut your mouth!”

Choi Byungil shouted, but Kim Junsu had already answered.

His face had gone completely pale. That was answer enough.

“Okay, Sangdong Guild. I figured as much.”

Choi Byungil’s face stiffened at my words.

“You shouldn’t have said that name out loud.”

“What, you’re going to kill me?”

“…I’ll capture you first and think about it.”

“That’ll be pretty hard.”

Choi Byungil’s Level was in the mid-sixties. His aura was comparable to Im Changsoo’s, while the others were ordinary C-ranks around Levels 30 or 40.

The odds of a group that wasn’t even a professional raid team managing to capture me were extremely low.

“Come at me prepared to die. That’s the only way you’ll manage to tie even a butterfly knot around my wrist.”

“Get him!”

At Choi Byungil’s shout, the Sangdong Guild watchers began charging at me from all directions.

Whoosh!

A dagger dropping toward my shoulder was the opening move.

I reached toward the trajectory that looked slow to me.

At the same time…

*Inventory open. Equip.*

Crunch!

A blade brimming with internal energy shattered the enemy’s dagger. Broken metal and someone’s blood spilled across the nameless weeds.

“Come on, you stalker bastards!”

Ssshhhhh!

[^1]: *Pyeong* is a traditional Korean unit of floor area; five pyeong is roughly 16.5 square meters.

[^2]: *Yeokmasal* is a traditional Korean notion of a fate that compels someone to wander. Here it also puns on *sal*, the Korean word used when asking someone’s age.
```
