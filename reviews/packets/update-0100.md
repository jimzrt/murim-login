<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0100.txt",
      "sha256": "16d10c097df214c39c729227ca27b6fa4586dd5c2583d3b95cb00902bacafc5e",
      "bytes": 16137
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5a4a9a6c4db0e4120add3840cf9902f4d6b07f553dd161a02b6b7a9724b1e9f5",
      "bytes": 3826
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "43155cc661a53ae1d57b2a0b798ab13bf82f30de31725512f2a5b24d91b69590",
      "bytes": 12286
    },
    {
      "path": "characters/Choi Byungil.md",
      "sha256": "5ecaa4fb4bb9a037c12ce717e603e30cccbf0bee1393bb5fa6fece7b30c3a9e5",
      "bytes": 593
    },
    {
      "path": "characters/Im Chunsoo.md",
      "sha256": "4cd6d9cff9646c982f9291c938d4bbf45890bed04345afa27e295812a08826de",
      "bytes": 666
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "17ab343bc131613c3b2a75efe81e7ae154392f99d3b080ac4f5d1e93a43d6b0b",
      "bytes": 23942
    },
    {
      "path": "characters/Kim Junsu.md",
      "sha256": "849b43b90cbd40dfbe504b721ccb5bb1d24a2cf5ec582ee23a2dfb4a4c31a1d2",
      "bytes": 603
    },
    {
      "path": "characters/Seong Jinho.md",
      "sha256": "43b08d7b4d083dacca998311f7f624559c84ed95ff96938efc7870da41f114d3",
      "bytes": 2027
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2a138293d44bcd3c51a3aaee395d9626043d669c531fd6eb8f5764828a0df576",
      "bytes": 11573
    }
  ],
  "estimated_tokens": 16874
}
-->

# Durable State Update — Chapter 100

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 100. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 100. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 100,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 100,
    "continuity_sources": [100],
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
    "Kim Junsu is a Level 41 C-rank mental mage who uses Familiars and is suffering from exhaustion and anxiety about his hair loss.",
    "Kim Gwondong is a Level 42 C-rank Security Team Hunter assigned to surveillance and disguises himself as a friendly neighbor.",
    "The Security Team has watched Taekyung for days and installed eavesdropping-magic Equipment in nearby real-estate offices.",
    "The Security Team uses a black Level 2 Cat Familiar to track Taekyung after he leaves home.",
    "Taekyung detects the black kitten as a Familiar and recognizes Kim Gwondong's disguise while concealing his suspicions.",
    "Taekyung learned of three properties traded within five days and five hundred meters of his home: Building 5, Unit 901; Building 4, Unit 302; and Building 3, Unit 202.",
    "Taekyung scanned the apartment complex and parking lot with Qi Sense and found no suspicious vehicles.",
    "The watchers are using one of the three recently traded apartments as a surveillance base, but the exact property remains unknown.",
    "Hong Woojin infiltrated Taekyung's home as a kitten Familiar and was recognized by Taekyung after Hayeon confined him.",
    "Hayeon left for the library, leaving Taekyung alone with the black and white Familiars.",
    "Taekyung searched his home with mana-detection Equipment and made a suspicious phone call as bait; the Security Team interpreted it as evidence of a secret plan and a USB.",
    "The Security Team's surveillance operation is being conducted under a special order from Guild Master Im Chunsoo.",
    "The Security Team Leader, Choi Byungil, orders an illegal attempt to subdue Taekyung and take the USB.",
    "Choi Byungil is a B-rank Hunter with a Level in the mid-sixties; the other five field watchers are C-rank Hunters around Levels 30 to 40.",
    "The two kitten Familiars are released after Taekyung's bait works, and Taekyung leads the watchers to a deserted mountain clearing.",
    "The USB is bait containing Taekyung's porn collection, stored in his Inventory.",
    "Hong Woojin maintains a hideout in a rooftop supply closet at Taekyung's apartment building and quits his assignment after observing the planned violence.",
    "Taekyung identifies the six watchers, confirms their Sangdong Guild affiliation, and begins fighting them after shattering an attacker's dagger."
  ],
  "continuity_sources": [
    98,
    99
  ],
  "open_questions": [
    "Why did Im Chunsoo issue a special warning about Taekyung?",
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Whether the Security Team's operation and Hong Woojin's investigation share the same commissioning chain remains unresolved.",
    "Who Taekyung called remains unknown."
  ],
  "safe_through": 99,
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
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |

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
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 사천     | **Sichuan**            |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 성진호 | **Seong Jinho** |
| 평화 | **Peace Guild** | Guild name. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |

## Listed compact profiles

### Choi Byungil.md

# Choi Byungil (최병일)

- **Safe through:** Chapter 99
- **Aliases:** None
- **Role:** B-rank Hunter and Security Team Leader of Sangdong Guild; leads the field operation against Jin Taekyung
- **Personality:** Ambitious, opportunistic, ruthless, and overconfident about his advantage over a C-rank Hunter
- **Voice:** Commanding, dismissive, profane, and calm when directing dangerous actions
- **Relationships:** Works under Guild Master Im Chunsoo; commands Kim Gwondong, Kim Junsu, and the other Security Team watchers

### Im Chunsoo.md

# Im Chunsoo (임춘수)

- **Safe through:** Chapter 99
- **Aliases:** Frozen
- **Role:** A-rank Hunter; founder and Guild Master of Sangdong Guild; renowned ice mage
- **Personality:** Intimidating, severe, and extremely short-tempered, though he has tried to moderate his temper with age
- **Voice:** Sharp and commanding, with a comparatively gentle tone when deliberately controlling his temper; becomes violently profane when enraged
- **Relationships:** Father of Im Changsoo, whom he considers a pathetic disappointment and immediately fires and punishes after learning of Changsoo's actions

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 99
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Kim Junsu.md

# Kim Junsu (김준수)

- **Safe through:** Chapter 99
- **Aliases:** None
- **Role:** Level 41 C-rank Hunter in Sangdong Guild’s Security Team; the Guild’s sole Familiar mage and a rare mental mage.
- **Personality:** Exhausted, anxious about his worsening hair loss, dutiful, and privately profane about his workload.
- **Voice:** Polite and restrained aloud; internally self-pitying, sarcastic, and profane.
- **Relationships:** Works under the unnamed Security Team Leader alongside Kim Gwondong and other surveillance Hunters.

### Seong Jinho.md

# Seong Jinho (성진호)

- **Safe through:** Chapter 88
- **Aliases:** Jinho; Mr. Seong Jinho
- **Role:** Manager of Hope Goshiwon; thirty-year-old exam candidate; civilian and Taekyung’s older friend
- **Personality:** Knowledgeable about IT, shamelessly blunt, melodramatic when threatened, and a heavy drinker
- **Voice:** Casual and teasing; invokes laws and hierarchy for comic effect; speaks informally to Taekyung while demanding respect as his older brother
- **Relationships:** Three years older than Jin Taekyung; treats him as a younger brother and drinking companion

## Korean source

```text
＃100화



사람은 저마다의 취미를 하나씩 갖고 있기 마련이다. 임춘수도 크게 다르지 않았다.

1팀장이 길드장실에 들어섰을 때 처음으로 목격한 것은 문을 향해 굴러오는 골프공이었다.

데구르르. 툭.

홀(Hole)을 한참이나 벗어난 공은 1팀장의 신발에 부딪힌 후에야 멈췄다. 허리를 숙여 공을 주우려는 그에게 임춘수가 손짓했다.

“됐어. 와서 차나 한잔해.”

“네.”

두 사람 사이에 잠깐 침묵이 흘렀다. 차를 음미하던 임춘수가 문득 입을 열었다.

“향 좋지?”

“아, 예. 좋은 차인가 봅니다.”

“이게 용정차라는 건데, 선물로 받았는데 사실 뭔지 잘 모르겠어. 가격만 더럽게 비싸고.”

“예?”

“뭘 그렇게 놀라?”

“차를 좋아하시는 줄 알았는데요.”

“전혀. 그냥 있어 보이고 싶어서 음미하는 흉내만 내는 거야. 집에서는 믹스 커피 마셔.”

1팀장은 실소를 흘렸다. 길드 간부들 사이에서 임춘수의 차(茶) 사랑은 유명했다. 누가 더 좋은 차를 길드장에게 선물하는지 경쟁이 붙을 정도다.

“놀랄 사람들이 몇 있겠군요.”

“예를 들자면?”

“3팀장이죠. 이번에 중국 출장 가서 명차를 구해 오겠다고 호언장담을 하고 다닙니다.”

“그놈 잘라. 일은 안 하고 풀떼기 구할 생각에 넋이 나갔구먼.”

“진심이십니까?”

“당연히 농담이지. 나는 농담도 못 하나?”

두 사람 사이로 가벼운 웃음이 흘렀다. 남은 찻물을 냉수처럼 쭉 들이켠 임춘수가 입맛을 다셨다.

“그래서, 언제 말할 건가?”

“예?”

“새로 가져온 소식 있잖아. 말하기 힘들어서 우물쭈물하는 놈한테 큰맘 먹고 비밀까지 얘기해 줬는데…….”

“그렇게 티가 났습니까?”

“앞으로는 들어오기 전에 거울 보고 와. 그렇게 죽상을 하고 있는데 누가 모르나.”

1팀장이 힘겹게 말문을 연 것은 얼마 지나지 않아서였다.

“일전에 내리신 평화 길드 조사…… 실패했습니다.”

“둘 다?”

“예. 죄송합니다.”

“더 자세히 설명해 봐.”

“신중하게 접근해 봤지만 평화 길드장과 팀장은 건드리지 않는 편이 좋을 것 같답니다.”

“그건 어느 정도 예상했어. 내가 직접 청탁을 넣었어야 했는데. 뭐, 결국 쓸데없는 체면 때문에 안 나선 거니까 내 탓도 있는 거지.”

“아닙니다. 제가 부족한 탓입니다.”

“그것도 맞는 말이고. 락 걸린 놈들은 몰라도 진태경인가 하는 C급 헌터는 성공했어야지.”

임춘수가 냉엄한 눈빛으로 그를 쏘아봤다.

“도대체 왜 실패한 건가? 외부에서 고용한 패밀리어 마법사에 길드 보안팀도 붙여 줬잖아.”

“저, 그게…….”

머뭇거리던 1팀장이 차마 하지 못했던 말을 어렵사리 토해 냈다.

“연락이 끊겼습니다.”

“응? 홍우진 그놈?”

“홍우진은 문자 한 통 남기고 잠적했고 연락이 끊긴 건 보안팀입니다.”

“보안팀이 왜? 주기적으로 상황 보고하지 않나?”

“네. 두 시간에 한 번씩 보고가 들어오는데…… 네 시간 전이 마지막입니다.”

“지금 보안팀이 단체 이탈이라도 했다는 소리야?”

“아닙니다. 정황상 진태경에게 당했을 확률이 높습니다.”

“뭐?”

이게 무슨 말인가.

황당해하는 임춘수에게 1팀장이 프린트해 온 종이를 내밀었다.

“오늘 자 보고입니다.”

특정 부분만 붉은 글씨로 칠해진 걸 보니 정기 보고서가 아니라 긴급 보고서다.

임춘수의 눈동자가 빠르게 활자 위를 누볐다.

표적이 정체를 알 수 없는 누군가와 통화를 했으며 대화 내용과 취한 행동 모두 수상하다. 보고를 빠짐없이 읽은 그가 한숨을 토해 냈다.

“허, 이거 생각보다 재밌는 놈이네. 그래서 이다음은?”

“보안팀장이 개인적으로 연락을 취했습니다. 급하게 표적을 쫓아야 하니 선 조치 후 보고 하겠다고요.”

“그리고 연락이 끊겼다…….”

임춘수는 골똘히 생각에 잠긴 채 탁자를 두드렸다.

톡. 톡. 톡. 고개를 들었을 때는 고급 원목 탁자가 꽁꽁 언 상태였다.

“진태경이랑 통화한 놈은 누구야? 이름 석 자 정도는 알아 왔으니까 이걸 보여 준 거겠지.”

“성진호. 부천 사는 30세 고시생입니다.”

“……1팀장아. 내가 잘못 들은 거냐? 헌터가 아니라 고시생?”

“저도 재차 확인해 봤지만 틀림없습니다. 진태경이 사는 고시원 총무더군요. 의형제 같은 사이랍니다.”

“허, 참. 오늘 여러 번 놀라게 만드는군.”

최소 A급 헌터는 될 줄 알았는데, 뭐? 민간인 고시생?

고개를 절레절레 내저은 임춘수가 자리에서 일어났다.

“끙, 이거 아주 제대로 당했네. 달랑 다섯 명 있는 길드가 뭐 이리 숨기는 게 많아?”

“어찌 하는 게 좋겠습니까?”

“어쩌긴 뭘 어째. 슬슬 밥시간인데 저녁이나 한 끼 하러 가야지.”

“……네?”

어리둥절한 1팀장을 본 임춘수가 혀를 찼다.

“잔말 말고 따라오기나 해.”

오늘 저녁은 일산에서 먹을 생각이다.



* * *



6대1의 싸움은 순식간에 끝났다.

애초에 나와 손을 섞을 수 있는 사람은 최병일 한 명뿐인데다가, 그마저도 오래 버티지 못하고 무릎을 꿇었다.

‘뭐, 당연한 거지.’

그러나 누군가에게는 커다란 충격이었던 것 같다.

양 발목이 부러진 최병일은 새하얗게 질린 얼굴로 계속해서 내게 말을 걸었다.

“A급 헌터? 정체를 숨긴 건가?”

“아닌데. 정체 숨긴 적 없는데.”

“진짜 소속을 밝혀라! 혹시 아레스 길드에서 우리 상동 길드를…….”

“나 평화 길드야. 그리고 아레스 길드는 당신네 길드에 관심도 없을걸. 체급부터가 완전히 다른데.”

“그럼 전화를 한 상대는 누구지?”

“고시원 총무 형이라고 몇 번을 말하냐. 성진호라고 하면 당신이 알아?”

“이럴 리가, 이럴 리가 없는데.”

결국 아가리 봉인술을 쓰는 수밖에 없었다. 그의 옷을 찢어 입을 틀어막은 뒤 그를 포함해 남은 부상자들을 모두 치료했다.

아, 물론 내가 스토어에서 샀던 포션은 아니다.

“이야, 상동 길드 지원 빵빵하네.”

당장 놈들이 들고 온 것만 털었는데도 장비며 소모품의 질과 양이 제법이다. 그중 일부를 치료에 쓰고 나머지는…….

“이건 일단 내가 압수. 혹시 불만 있는 사람?”

당연하게도 누구 하나 손을 들지 않았다.

다들 압도적인 내 무력에 질렸는지 상처가 치료됐음에도 감히 다시 덤빌 생각을 하지 못했다. 상당히 똑똑한 놈들이다.

“자, 이제 나한테 너희들의 임무에 대해서 상세히 알려 줄 사람?”

이번 역시 아무도 손을 들지 않아서 직접 고르는 수밖에 없었다.

선택은 아주 쉬웠다.

“너.”

“저, 저요?”

“응, 너.”

패밀리어 마법사, 김준수는 움찔하더니 이내 결연한 표정으로 선언했다.

“저는 보안팀 소속입니다. 길드의 기밀 사항을 외부인에게 함부로 유출할 수 없습니다.”

“오.”

나는 감탄했고, 그것과 동시에 녀석의 머리끄덩이를 잡아당겼다.

어디선가 테이프 뜯어지는 작은 소리가 들리고 가발이 훌렁 벗겨졌다. 그러자 그 아래 감춰져 있던 빛나는 정수리가 드러난다.

“이게 무슨!”

“자, 지금부터 하는 질문에 거짓말이나 모르쇠로 일관할 시 머리털을 한 움큼씩 뽑도록 하겠다.”

“……!”

그 후부터는 일사천리였다. 어떻게 해서든 머리를 지키고 싶은 탈모인의 입에서 온갖 정보가 흘러나왔다.

“홍우진?”

“네, 1팀장님이 외부에서 고용한 B급 마법사입니다. 저처럼 패밀리어 마법이 주특기고요.”

“그래?”

아깝다. 그놈도 잡아서 족쳤어야 했는데.

‘언젠가 만날 일이 오겠지. 오래 걸리면 내가 찾아내도 되고.’

나는 입맛을 다시며 계속해서 정보를 뽑아냈다. 김준수가 멈칫한다 싶으면 얼마 남지 않은 머리카락을 만지작거리며 용기를 북돋아 주었다.

“끝입니다, 진짜 끝. 아무리 제가 보안팀이라지만 더 이상은 몰라요. 그러니 제발 머리카락만큼은…….”

억울함과 진심이 묻어 나오는 말투다. 특히 마지막 말이 내 심금을 울렸다.

‘이 정도면 얼추 마무리됐겠지.’

배후는 예상대로 상동 길드, 정확히 말하면 임춘수였다.

가뜩이나 흥청망청 사는 아들내미가 수입 억을 삥 뜯긴 걸 보고 그 직후부터 우리 길드를 털기 시작한 거다.

뭐, 결국 나한테 역으로 털렸지만.

“길드장님께서 가만히 있지 않을 거다.”

“약한 놈들 전용 멘트, 뭐 그런 거라도 있나? 길드장 운운하지 말고 본인이 싼 똥이나 치울 생각해.”

“……큭.”

내 일침에 최병일은 분한 듯 고개를 떨궜지만 저 인간의 말이 아주 틀린 건 아니다.

‘상동 길드장이 알면 열 좀 받겠네.’

감시하라고 부하들을 보냈더니 오히려 역으로 털리고 붙잡히는 신세까지 됐다. 길드장은 물론이고 길드 전체 입장에서 봐도 이런 개망신이 또 없다.

사안이 사안이니만큼 그쪽에서도 조용히 덮고 넘어가 주길 바랄 뿐이다.

‘최 팀장한테 전화를 해야 하나.’

스마트폰을 들고 고민하던 찰나였다.



[010-xxxx-xxxx]



처음 보는 번호로 걸려 온 한 통의 전화. 뭐지?

왠지 모르게 드는 묘한 긴장감 속에 전화를 받았다.

“여보세요?”

- 내려오게. 밑에서 기다리고 있네.

“네? 전화 잘못 거신 것 같은데요.”

- 진태경. 맞지?

“아니, 맞긴 한데…… 누구세요?”

- 나 임춘수라고 하는 사람인데, 그쪽이 우리 애들을 몇 명 데리고 있다고 해서.

“…….”

- 듣고 있나?

듣고는 있다. 말을 못 할 뿐이지.

중견 길드의 길드장이 나를 만나기 위해 여기까지 직접 행차하실 줄이야. 그것도 성질 더럽다는 임춘수가.

- 내려와, 오해도 풀 겸 밥이나 한 끼 하게.

굳이 오해를 풀 만한 일은 없지만 ‘싫어요.’라고 했을 경우 무슨 일이 벌어질지 모르겠다.

이미 위치까지 파악하고 온 양반 아닌가?

결국 내 선택지는 하나밖에 없었다.

“지금 내려가겠습니다.”



* * *



임춘수의 첫인상은 강렬했다. 생각보다 젊었고 눈빛은 온화한 듯하면서도 뜨거웠다.

‘불같다.’

아이러니하게도 저것이 얼음 마법의 대가를 만나서 처음으로 한 생각이었다.

“안녕하십니까. 진태경이라고 합니다.”

“임춘수라고 하네.”

뜨거운 눈빛과는 달리 목소리는 차갑다. 이제야 프로즌(frozen)이라는 별명과 어울리는 사람이 된 것 같았다.

“보고서 사진으로만 보던 얼굴을 이렇게 보니까 좀 신기하군.”

뒤를 캤다는 걸 이렇게 직설적으로, 부끄러워하지 않고 말할 수 있는 사람도 존재하는구나.

“우리 애들은?”

“위에 있습니다.”

“사망자가 있나?”

“설마요. 범죄자 되는 건 딱 질색입니다.”

“그거 고맙군.”

임춘수가 나를 향해 고개를 까딱였다.

“우리 애들이 조급함에 실수를 저질렀네. 이해해 줄 텐가?”

“적당한 보상이 있다면요.”

내 대답에 임춘수는 피식 웃었고, 팀장처럼 보이는 옆의 남자는 눈살을 찌푸렸다.

“젊은 친구가 예의가 없군.”

“제가 좀 그런 편이긴 한데…… 감시까지 붙인 분들한테 들으니까 기분이 좀 묘하네요.”

“아무리 그래도.”

남자의 말은 이어지지 못했다. 임창수가 손을 들어 그를 제지했기 때문이었다.

“1팀장은 위에 가서 애들이나 풀어 줘.”

“……예. 길드장님.”

김 집사가 부드러운 카리스마라면 그는 거친 카리스마의 소유자였다. 같은 마법사라 그런 걸까? 어쩐지 모르게 두 사람의 모습이 겹쳐 보였다.

“자네는 나랑 좀 걷지.”

임창수가 앞장섰고 내가 그 뒤를 따랐다.

“혹시 그거 알고 있나?”

한동안 거침없이 걸어가던 임춘수가 불쑥 말문을 열었다.

“난 일단 원한 관계가 맺어지면 무조건 끝을 봐야 해. 자네는 어떨지 모르지만 난 그런 성격이지.”

무림 스타일인데?

약육강식. 적자생존. 이 아저씨의 혈관에도 무림 터프가이의 피가 흐르는 모양이다.

“지금의 상동 길드는 그렇게 쌓아 올린 거야. 무너트린 걸 밟고 건져 내서 더 높게.”

“그렇군요.”

“평화 길드는 어떤가?”

“……그게 무슨 뜻입니까?”

“근 10년은 무료했지. 인근 길드와는 전부 동맹 관계고 우리에게 더 이상 적수가 없었어. 그런데 자네들이 나타난 거야.”

호기심과 열정이 끓어오르고 있는 듯한 그의 눈을 보며 드는 생각은 딱 하나였다.

‘이거 위험한데.’

그러거나 말거나 임춘수의 말은 이어졌다.

“길드장과 팀장은 나로서도 정보를 쉽게 열람할 수 없는 인물들이고…… 무엇보다 자네의 존재가 날 자극시켰어.”

우리는 이제 언덕길을 오르고 있었다. 적지 않은 나이임에도 불구하고 임춘수는 숨이 차는 것 같지 않았다.

“자네는 내가 왜 여기까지 왔는지 알고 있나?”

“절 보기 위해서겠죠.”

“절반만 맞췄어.”

임춘수의 발걸음이 멎었다. 천천히 돌아서는 그의 전신에서 서늘한 냉기가 흘러나왔다.



[Lv.75 임춘수]



“내 나이에는 시간이 금이야. 얼굴만 보려고 여기까지 올 만큼 사치스러운 사람이 아닐세.”

프로즌. 대격변을 온몸으로 헤쳐 나간 노련한 A급 마법사가 나를 향해 손을 펼친 순간.

츠츠츠.

아무것도 없던 머리 위 허공에서 십여 개의 얼음송곳이 생겨났다. 한여름의 공기가 얼어붙고 뜨겁게 달궈진 흙길에 서리가 내려앉는다.

‘된통 걸렸군.’

제법 경우를 아는 노인네라고 생각했는데, 설마 다짜고짜 이런 식으로 나올 줄은 몰랐다.

“이렇게까지 해야 됩니까?”

“자네라서 이렇게까지 하는 거야.”

“저는 고작 C급인데요.”

“그래, 그 C급 헌터 실력 좀 보자고.”

말이 끝남과 동시에 임춘수가 주먹을 움켜쥐었다. 시린 냉기를 뿜어내는 얼음송곳들이 나를 향해 쏘아졌다.

쐐애애애액!

그러나 얼음송곳은 내 옷자락 하나 건드리지 못했다.

“솟구쳐라. 파이어 월(Fire Wall).”

또렷한 음성과 함께 대기에 스며든 마나가 요동친다. 임춘수의 마법으로 서리가 끼어 있던 바닥이 녹고 불꽃이 솟구쳤다.

화륵, 화아악!

그건 말 그대로 불의 장벽이었다. 푸른 화염은 얼음송곳을 집어삼키고 나와 임춘수의 사이를 갈랐다.

일렁이는 불꽃 너머, 임춘수가 경악에 찬 음성을 토해 냈다.

“이건……!”

그러나 내가 보고 있는 것은 임춘수가 아니었다. 그의 등 뒤, 등산로 입구에 서 있던 한 사람이 부드러운 목소리로 인사를 건넸다.

“늦지 않아서 다행입니다. 춘수, 자네도.”



[Lv.80 김화종]



김화종. 김 집사의 등장이었다.
```

## Final English reading copy

```markdown
# Chapter 100

Everyone had at least one hobby. Im Chunsoo was no different.

The first thing Team Leader 1 saw when he entered the Guild Master’s office was a golf ball rolling toward the door.

Roll, roll. Thunk.

The ball had rolled far wide of the hole and only stopped after striking Team Leader 1’s shoe. As he bent down to pick it up, Im Chunsoo waved him off.

“Forget it. Come over here and have some tea.”

“Yes, sir.”

A brief silence passed between them. After savoring his tea, Im Chunsoo suddenly spoke.

“Smells good, doesn’t it?”

“Ah, yes. I suppose it must be good tea.”

“This is Longjing tea. I received it as a gift, but to be honest, I don’t really know what it is. It’s just filthy expensive.”

“What?”

“Why are you so surprised?”

“I thought you liked tea.”

“Not at all. I only pretend to savor it because I want to look sophisticated. At home, I drink instant coffee.”

Team Leader 1 let out a quiet laugh. Im Chunsoo’s love of tea was famous among the Guild executives. They had even begun competing to see who could give the Guild Master the better tea.

“A few people are going to be surprised.”

“For example?”

“Team Leader 3. He’s been bragging that he’ll bring back some famous tea from his upcoming business trip to China.”

“Fire that bastard. He’s lost his mind thinking about gathering weeds instead of doing his job.”

“You’re serious?”

“Of course I’m joking. Am I not allowed to joke?”

Light laughter passed between them. Im Chunsoo gulped down the remaining tea as if it were cold water, then smacked his lips.

“So, when are you going to tell me?”

“Tell you what?”

“You have some new information. I went out of my way to tell you a secret because you were having trouble speaking up…”

“Was it that obvious?”

“Look in a mirror before you come in next time. With a long face like that, anyone could tell.”

It wasn’t long before Team Leader 1 finally managed to speak.

“The investigation into the Peace Guild that you ordered previously… has failed.”

“Both of them?”

“Yes. I’m sorry.”

“Explain in more detail.”

“They approached carefully, but they say it would be better not to provoke the Peace Guild Master or Team Leader.”

“I expected as much. I should have made the request personally. In the end, I didn’t step in because of my useless pride, so some of the blame is mine.”

“No, it was because I was inadequate.”

“That’s true, too. Even if those locked-down bastards were out of reach, this C-rank Hunter named Jin Taekyung should have been a success.”

Im Chunsoo shot him a cold glare.

“Why exactly did you fail? I gave you a Familiar mage hired from outside and even assigned the Guild’s Security Team to him.”

“Well, that…”

Team Leader 1 hesitated, then finally forced out the words he had been unable to say.

“We lost contact.”

“Hm? That bastard Hong Woojin?”

“Hong Woojin disappeared after leaving a single text message. The ones we lost contact with were the Security Team.”

“Why the Security Team? Don’t they report the situation regularly?”

“Yes. Reports come in every two hours, but… the last one was four hours ago.”

“Are you saying the entire Security Team walked out on us?”

“No. Judging by the circumstances, it’s highly likely Jin Taekyung got to them.”

“What?”

What was that supposed to mean?

As Im Chunsoo stared at him in disbelief, Team Leader 1 handed him the pages he had printed out.

“Today’s report.”

The fact that only certain sections had been highlighted in red showed that this was an emergency report, not a regular one.

Im Chunsoo’s eyes raced across the words.

The target had spoken on the phone with someone whose identity was unknown, and both the contents of the conversation and the target’s actions were suspicious. After reading the report from beginning to end, Im Chunsoo let out a sigh.

“Hah. He’s more interesting than I expected. What happened next?”

“The Security Team Leader contacted me directly. He said they needed to pursue the target immediately, so he would take action first and report afterward.”

“And then they lost contact…”

Im Chunsoo fell deep into thought as he tapped the table.

Tap. Tap. Tap.

When he raised his head, the high-quality wooden table had frozen solid.

“Who did Jin Taekyung call? You found out at least the person’s full name, or you wouldn’t have shown me this.”

“Seong Jinho. A thirty-year-old exam candidate living in Bucheon.”

“……Team Leader 1. Did I hear you wrong? An exam candidate, not a Hunter?”

“I checked again myself, but there’s no mistake. He’s the manager of the goshiwon where Jin Taekyung lives. They’re supposedly like sworn brothers.”

“Hah. Today keeps surprising me.”

Im Chunsoo had expected him to be at least an A-rank Hunter. But what was this? A civilian exam candidate?

Shaking his head, Im Chunsoo rose from his seat.

“Ugh, we really got played. How does a Guild with only five people have so much to hide?”

“What should we do?”

“What do you mean, what should we do? It’s almost dinnertime. We should go have a meal.”

“……What?”

Im Chunsoo clicked his tongue at the bewildered Team Leader 1.

“Stop talking and follow me.”

He was thinking of having dinner in Ilsan that evening.

* * *

The six-on-one fight ended in an instant.

To begin with, Choi Byungil was the only one who could exchange blows with me. Even he didn’t last long before dropping to his knees.

*Obviously.*

But it seemed to have been a tremendous shock to someone.

With both ankles broken, Choi Byungil continued talking to me with a face as white as a sheet.

“An A-rank Hunter? Were you hiding your identity?”

“No. I never hid my identity.”

“Tell me your real affiliation! Is Ares Guild making a move against our Sangdong Guild…?”

“I’m with the Peace Guild. And Ares Guild wouldn’t be interested in your Guild. You’re in completely different weight classes.”

“Then who was the person you called?”

“How many times do I have to tell you? He’s my goshiwon manager hyung. Would you know him if I said his name was Seong Jinho?”

“This can’t be. This can’t be happening.”

In the end, there was nothing for it but to use the mouth-sealing technique. I tore his clothes into strips and gagged him, then treated all the remaining wounded, including him.

Of course, I didn’t use the potions I had bought from the Store.

“Wow, Sangdong Guild gives you guys some serious support.”

Even after looting only what they had brought with them, the quality and quantity of their Equipment and consumables were nothing to sneeze at. I used some of them for treatment, and the rest…

“I’m confiscating this for now. Anyone have a problem with that?”

Naturally, no one raised a hand.

They must have been so intimidated by my overwhelming strength that, even after their injuries had been healed, they didn’t dare attack me again. They were fairly smart men.

“Now, who wants to tell me all about your mission?”

Once again, nobody raised a hand, so I had to choose someone myself.

The choice was easy.

“You.”

“M-me?”

“Yeah, you.”

The Familiar mage, Kim Junsu, flinched. Then he declared with a resolute expression,

“I’m with the Security Team. I cannot carelessly disclose the Guild’s confidential information to an outsider.”

“Oh.”

I was impressed. At the same time, I grabbed him by the hair and yanked.

A small sound like tape being ripped came from somewhere, and his wig came clean off. The gleaming bald crown hidden beneath it was exposed.

“What is this?!”

“From now on, if you lie or keep claiming ignorance in response to my questions, I’ll pluck your hair out by the handful.”

“……!”

After that, everything proceeded smoothly. All kinds of information poured from the mouth of a balding man desperate to protect his hair by any means necessary.

“Hong Woojin?”

“Yes. He’s a B-rank mage hired from outside by Team Leader 1. Like me, his specialty is Familiar magic.”

“Really?”

What a waste. I should have caught that bastard and beaten the information out of him, too.

*I’ll run into him someday. If it takes too long, I can always track him down myself.*

Smacking my lips, I continued extracting information. Whenever Kim Junsu seemed to hesitate, I encouraged him by fiddling with his remaining hair.

“That’s everything. I really mean it, that’s all. Even though I’m in the Security Team, I truly don’t know anything else. So please, just leave my hair alone…”

His tone was full of both resentment and sincerity. The final words in particular struck a chord with me.

*This should be more or less everything.*

The mastermind behind it was the Sangdong Guild—or, more precisely, Im Chunsoo.

After seeing that his spendthrift son had been shaken down for a hundred million won in income, he had started digging into our Guild.

Well, in the end, I was the one who robbed him instead.

“The Guild Master won’t let this go.”

“Is that some line reserved for weaklings? Forget invoking the Guild Master and clean up the shit you made yourself.”

“……Tch.”

At my sharp retort, Choi Byungil lowered his head in frustration. But the man wasn’t entirely wrong.

*The Sangdong Guild Master is going to be pretty pissed when he finds out.*

He had sent his subordinates to watch me, only for them to get robbed and captured instead. For the Guild Master—and the Guild as a whole—this was about as fucking humiliating as it got.

Given the seriousness of the matter, I could only hope they would quietly bury it and move on.

*Should I call Team Leader Choi?*

That was when it happened.

010-xxxx-xxxx

A call from a number I didn’t recognize.

What was this?

A strange tension rose within me for no apparent reason as I answered.

“Hello?”

“Come downstairs. I’m waiting below.”

“Huh? I think you have the wrong number.”

“Jin Taekyung. That’s right, isn’t it?”

“Well, yes, but… who are you?”

“My name is Im Chunsoo. I heard you have a few of my people with you.”

“……”

“Are you listening?”

I was listening. I just couldn’t speak.

The Guild Master of a mid-sized Guild had come all the way here himself to meet me. And it was Im Chunsoo, of all people—the man with the terrible temper.

“Come down. We can clear up any misunderstandings over a meal.”

There was no misunderstanding that needed clearing up, but I had no idea what would happen if I said, *No.*

Hadn’t the man already found out my location?

In the end, I had only one option.

“I’ll be down shortly.”

* * *

Im Chunsoo’s first impression was intense. He was younger than I expected, and although his eyes seemed gentle, they burned with heat.

*Fiery.*

Ironically, that was my first thought upon meeting a master of ice magic.

“Hello. My name is Jin Taekyung.”

“I’m Im Chunsoo.”

His voice was cold, unlike his burning gaze. At last, he seemed like someone who deserved the nickname Frozen.

“It’s interesting to see in person the face I’d only seen in report photos.”

There were actually people who could admit so bluntly and without embarrassment that they had dug into my background.

“What about my people?”

“They’re upstairs.”

“Are there any fatalities?”

“Of course not. I have no desire to become a criminal.”

“I appreciate that.”

Im Chunsoo gave me a slight nod.

“My people got impatient and made a mistake. Can you let it slide?”

“If there’s reasonable compensation.”

Im Chunsoo let out a quiet laugh, and the man beside him, who looked like a Team Leader, frowned.

“Young man, you’re rude.”

“I am, somewhat… but hearing that from someone who even put me under surveillance feels a little strange.”

“Even so—”

The man couldn’t continue. Im Changsoo raised a hand to stop him.

“Team Leader 1, go upstairs and release my people.”

“……Yes, Guild Master.”

If Kim Butler possessed a gentle charisma, this man possessed a rough one. Maybe it was because they were both mages. Somehow, the two men overlapped in my mind.

“Come take a walk with me.”

Im Changsoo went ahead, and I followed behind him.

“Do you know something?”

After walking briskly for a while, Im Chunsoo suddenly spoke.

“Once I have a grudge against someone, I have to see it through to the end. I don’t know about you, but that’s the kind of person I am.”

*Very Murim of him.*

The strong devour the weak. Survival of the fittest. It seemed the blood of a Murim tough guy flowed through this man’s veins, too.

“That’s how I built the Sangdong Guild. I climbed higher by stepping on what I had brought down and salvaging whatever I could.”

“I see.”

“What about the Peace Guild?”

“……What do you mean?”

“The past decade has been dull. We’re allies with every nearby Guild, and we haven’t had a rival for a long time. Then you people appeared.”

As I looked into his eyes, where curiosity and passion seemed to be boiling, I had only one thought.

*This is dangerous.*

Whether I cared or not, Im Chunsoo continued speaking.

“Your Guild Master and Team Leader are people whose information I can’t easily access myself… But more than anything, your existence has stirred me up.”

We were climbing a hill now. Despite his considerable age, Im Chunsoo didn’t seem short of breath.

“Do you know why I came all the way here?”

“To see me.”

“You’re only half right.”

Im Chunsoo’s footsteps stopped. Slowly turning around, he released a frigid chill from his entire body.

> **System**
>
> Level 75 Im Chunsoo

“At my age, time is money. I’m not so indulgent that I’d come all the way here just to see your face.”

Frozen. The seasoned A-rank mage who had fought his way through the Great Cataclysm himself.

The moment he extended his hand toward me—

Hissssss.

Around a dozen ice spikes formed in the empty air above my head. The midsummer air froze, and frost settled over the scorching dirt path.

*I’d been well and truly caught.*

I had thought he was an old man with some sense of propriety. I never imagined he would launch straight into something like this.

“Do you really have to go this far?”

“I’m going this far because it’s you.”

“I’m only a C-rank.”

“Exactly. I want to see what that C-rank Hunter can do.”

The moment he finished speaking, Im Chunsoo clenched his fist. The ice spikes, streaming with biting cold, shot toward me.

Whoosh!

But they couldn’t even touch the hem of my clothes.

“Rise up. Fire Wall.”

At the sound of a clear voice, the mana permeating the air began to churn. The ground, which had been frosted over by Im Chunsoo’s magic, melted as flames surged upward.

Fwoosh! Fwoosh!

It was exactly what its name suggested: a wall of fire. Blue flames swallowed the ice spikes and split the space between Im Chunsoo and me.

Beyond the wavering flames, Im Chunsoo cried out in shock.

“What is this…!”

But I wasn’t looking at Im Chunsoo.

Behind him, a man standing at the entrance to the hiking trail greeted me in a gentle voice.

“I’m glad I’m not late. Chunsoo, you’re here too.”

> **System**
>
> Level 80 Kim Hwajong

Kim Hwajong.

Kim Butler had arrived.
```
